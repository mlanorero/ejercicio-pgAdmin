from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
from models import db, User, Post
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:contraseña@localhost:5432/postgres'
app.congig['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config['DEBUG']=True

db.init_app=(app)
Migrate(app, db)

