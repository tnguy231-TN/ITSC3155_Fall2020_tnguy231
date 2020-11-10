# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template

from flask import request
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# Initialize the Flask-SQLAlchemy extension instance
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_note_app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#  Bind SQLAlchemy db object to this Flask app
db.init_app(app)

# Setup models
with app.app_context():
    db.create_all()   # run under the app context

