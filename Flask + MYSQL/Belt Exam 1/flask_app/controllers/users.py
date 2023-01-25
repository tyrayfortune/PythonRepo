import re
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.magazine import  Magazine

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

## TODO handle registration with bcrypt
@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    session['name'] = request.form['first_name']
    return redirect("/dashboard")

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['name'] = user_in_db.first_name
    return redirect("/dashboard")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


@app.route('/user/accountss/<int:id>')
def  user_accounts(id):
    data ={ 
        "id":id
    }
    
    return render_template("user_account.html", magazine=Magazine.get_one(data), user=User.get_one(data))

@app.route('/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("dashboard.html", magazine=Magazine.get_one(data))

@app.route('/user/create',methods=['POST'])
def created():
    print(request.form)
    if not Magazine.validate_recipe(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/magazine/create')
    # else no errors:
    Magazine.save(request.form)
    return redirect('/dashboard')

@app.route('/destroy/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        flash("please sign in/register")
        return redirect ('/')
    data ={
        'id': id
    }
    Magazine.destroy(data)
    return redirect('/dashboard')