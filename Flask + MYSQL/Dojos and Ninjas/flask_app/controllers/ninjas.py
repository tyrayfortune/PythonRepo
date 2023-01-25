from flask_app import app

from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninja_index():    
    return render_template("ninjas.html", dojos = Dojo.get_all())

@app.route('/create/ninja', methods=["POST"])
def new_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(f"/dojo/{request.form['dojo_id']}")
