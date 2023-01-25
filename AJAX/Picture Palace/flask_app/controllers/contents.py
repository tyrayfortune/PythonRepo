from flask_app import app, Bcrypt
from flask import render_template, request, redirect, session, flash
import PIL
from flask_app.models.content import Content
from flask_app.models.user import User
import base64

##!CREATE
## TODO Show the new content form
@app.route('/contents/new')
def new_content():
    return render_template('new_content.html')

## TODO handle new content form
@app.route('/create/content', methods=['POST'])
def create_content():
    print(request.form)
    content = Content.save(request.form) #! class method in content class, find it in ../controllers/content.py
    print(content)
    return redirect("/homepage")


##! READ
@app.route('/homepage')
def dashboard():
    # get_image = Content.get_image()
    contents = Content.get_all()
    print(contents[0].image)
    return render_template('homepage.html', contents = contents)

@app.route('/contents/<int:id>')
def show_content(id):
    data = {'id': id}
    return render_template('show_content.html', content = Content.get_one(data))


#! UPDATE
## TODO route to edit content form
@app.route('/contents/<int:id>/edit')
def edit_content(id):
    data = {'id': id}
    content = content.get_one(data)
    return render_template('edit_content.html', content = content)

## TODO handle content edit
@app.route('/edit/content', methods=['POST'])
def update_content():
    print(request.form)
    content = Content.update(request.form)
    print(content)
    return redirect(f"/contents/{request.form['id']}")