import requests
import json
import time
import os

from flask import Flask, render_template, flash, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['DEBUG'] = config('DEBUG')
app.config['BASE_DIR'] = os.path.abspath(os.path.dirname(__file__))  
app.config['DATABASE_CONNECT_OPTIONS'] = {}
app.config['CSRF_SESSION_KEY'] = config('SECRET_KEY')
app.config['SECRET_KEY'] = config('SECRET_KEY')
app.config['CSRF_SESSION_KEY'] = config('SECRET_KEY')
app.config['CSRF_ENABLED'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = config('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CSRF_ENABLED'] = True
app.config['THREADS_PER_PAGE'] = 2

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


@app.route('/')
def home():
    data_ = {
        "Project Name": "Awas Lubang API"
    }
    return jsonify(data_)

@app.errorhandler(404)
def not_found(error):
    return "404", 404


from apps.aduan.controllers import aduan_bp as aduan_module
app.register_blueprint(aduan_module)   
 

db.create_all()