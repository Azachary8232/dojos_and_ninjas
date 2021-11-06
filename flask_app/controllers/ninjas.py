# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_ninja
from flask_app.models.model_dojo import Dojo



@app.route('/ninjas')
def ninjas():
    data = Dojo.get_all()
    print(data)
    return render_template('create_ninja.html', dojos = data)


@app.route('/ninja/<int:id>')
def ninja():
    return render_template('dojos.html')

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    dojo_id = request.form['dojo_id'] 
    model_ninja.Ninja.create(request.form)
    return redirect(f'/dojo/{dojo_id}')