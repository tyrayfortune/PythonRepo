import re
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash, json
from flask_app.models.user import User


bcrypt = Bcrypt(app)

# Login
@app.route('/')
def index():
    return render_template("login.html")

    ## TODO LOGIN HANDLER
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
    session['user_name'] = user_in_db.first_name
    return redirect("/homepage")

# register
@app.route('/register')
def register():
    return render_template("register.html")
    
## TODO REGISTRATION HANDLER
@app.route('/register/user', methods=['POST'])
def register_user():
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
    session['user_name'] = request.form['first_name']
    return redirect("/homepage")

# HOMEPAGE
# @app.route('/homepage')
# def homepage():
#     return render_template("homepage.html")



@app.route('/users/<int:id>')
def show_user(id):
    data = {'id': id}
    user = User.get_user_with_models(data)
    return render_template("show_user.html", user = user)
    


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')





