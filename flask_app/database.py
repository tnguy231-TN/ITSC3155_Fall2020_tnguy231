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


