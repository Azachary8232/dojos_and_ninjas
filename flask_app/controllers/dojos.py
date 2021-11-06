from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_dojo import Dojo

@app.route('/')
def index():
    return render_template('dojo_info.html')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos = Dojo.get_all())

@app.route('/dojo/<int:id>')
def dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo_info.html', dojo=Dojo.get_one_with_ninjas(data))

@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    data = {
        "location" : request.form['location']
    }
    Dojo.create(data)
    return redirect('/dojos')