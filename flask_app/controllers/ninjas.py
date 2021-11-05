# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_ninja import Ninja

@app.route('/')
def index():
    return render_template('dojo_info.html')

@app.route('/ninjas')
def ninjas():
    return render_template('dojo_info.html')


@app.route('/ninja/<int:id>')
def ninja():
    return render_template('dojos.html')

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    data = {
        "(something/no())" : request.form['(somethong/no())']
    }
    Ninja.save(data)
    return redirect('/ninja)')