# all @app.route() functions

from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.(user/no()) import (User/no())

@app.route('/*user*')
def users():
    return render_template('index.html')

@app.route('/create/(user/no())', methods=['POST'])
def create_(user/no())():
    data = {
        "(something/no())" : requestform['(somethong/no())']
    }
    (User/no()).save(data)
    return redirect('/*user*)')