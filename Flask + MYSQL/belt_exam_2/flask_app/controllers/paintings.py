from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.painting import Painting

##!CREATE
## TODO Show the new painting form
@app.route('/paintings/new')
def new_painting():
    if 'user_id' not in session:
        flash("please sign in/register")
        return redirect ('/')
    return render_template('new_painting.html')

## TODO handle new painting form
@app.route('/painting/create', methods=['POST'])
def create_painting():
    print(request.form)
    if not Painting.validate_painting(request.form):
        return redirect('/paintings/new')
    painting = Painting.save(request.form) #! class method in painting class, find it in ../controllers/painting.py
    print(painting)
    return redirect('/paintings')


##! READ
@app.route('/paintings')
def dashboard():
    if 'user_id' not in session:
        flash("please sign in/register")
        return redirect ('/')
    return render_template('paintings.html', paintings = Painting.get_all())

@app.route('/paintings/<int:id>')
def show_painting(id):
    data = {'id': id}
    return render_template('show_painting.html', painting = Painting.get_one(data))


#! UPDATE
## TODO route to edit painting form
@app.route('/painting/edit/<int:id>')
def edit_painting(id):
    data = {'id': id}
    painting = Painting.get_one(data)
    return render_template('edit_painting.html', painting = painting)


@app.route('/edit/painting', methods=['POST'])
def update_painting():
    print(request.form)
    if not Painting.validate_painting(request.form):
        return redirect('/paintings/new')
    painting = Painting.update(request.form)
    print(painting)
    return redirect("/paintings")

@app.route('/destroy/<int:id>')
def destroy_painting(id):
    data = {'id':id}
    Painting.destroy(data)   #! class method in User class, find it in ../controllers/user.py
    return redirect('/paintings')