from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_dojo import Dojo

@app.route('/')
def index():
    return render_template('dojo_info.html')

@app.route('/dojos')
def users():
    return render_template('dojos.html', dojos = Dojo.get_all())

@app.route('/dojo/<int:id>')
def dojo():
    return render_template('dojo_info.html')

@app.route('/dojo/create', methods=['POST'])
def create_ninja():
    data = {
        "(something/no())" : request.form['(somethong/no())']
    }
    Dojo.save(data)
    return redirect('/ninja)')