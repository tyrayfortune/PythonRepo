import re
from flask_app import app, Bcrypt
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.magazine import  Magazine

@app.route('/dashboard')
def dashboard():
    magazines = Magazine.get_all()
    print(magazines)
    if 'user_id' not in session:
        flash("please sign in/register")
        return redirect ('/')
    return render_template('dashboard.html', magazines = Magazine.get_all())


@app.route('/new')
def add_magazine():
    return render_template('new.html')

@app.route('/magazine/create',methods=['POST'])
def create():
    print(request.form)
    if not Magazine.validate_magazine(request.form):
        # redirect to the route where the magazine form is rendered.
        return redirect('/new')
    # else no errors:
    Magazine.save(request.form)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    
    return render_template("show.html", magazine=Magazine.get_one(data))

