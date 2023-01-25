import re
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

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


# recipe controllers start here

@app.route('/dashboard')
def dashboard():
    recipes = Recipe.get_all()
    print(recipes)
    return render_template('dashboard.html', recipes = Recipe.get_all())

@app.route('/recipes/new')
def recipes_new():
    return render_template('recipes_new.html')

@app.route('/recipe/create',methods=['POST'])
def create():
    print(request.form)

    if not Recipe.validate_recipe(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/recipes/new')
    # else no errors:
    Recipe.save(request.form)
    return redirect('/dashboard')

@app.route('/destroy/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        flash("please sign in/register")
        return redirect ('/')
    data ={
        'id': id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    
    return render_template("edit_recipe.html",recipe=Recipe.get_one(data))

@app.route('/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("recipe_show.html", recipe=Recipe.get_one(data))