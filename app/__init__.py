from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/registerbook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from app.routes import route