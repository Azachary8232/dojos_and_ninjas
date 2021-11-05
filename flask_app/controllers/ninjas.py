# all @app.route() functions

from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_ninja import Ninja

@app.route('/')
def index():
    return render_template('dojos.html')

@app.route('/ninja')
def users():
    return render_template('index.html')

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    data = {
        "(something/no())" : request.form['(somethong/no())']
    }
    Ninja.save(data)
    return redirect('/ninja)')