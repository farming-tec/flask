# -*- coding: utf-8 -*-
from os import environ
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_dotenv import DotEnv
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_mongoengine.wtf import model_form
from markupsafe import escape 

# Init modules
env = DotEnv()
db = MongoEngine()

# Flask setup
app = Flask(__name__)
env.init_app(app, env_file="/var/www/html/frontend/.env" )
app.config['MONGODB_SETTINGS'] = {
    'db': app.config["MONGO_DATABASE_NAME"],
    'port': int(app.config["MONGO_HOST_PORT"]),
    'host': '0.0.0.0',
    'username':app.config["MONGO_CROP_USERNAME"],
    'password':app.config["MONGO_CROP_PASSWORD"]
}
db.init_app(app)
CORS(app)


@app.route('/')
def home():
    return 'Hello Python!'


@app.route('/user/<username>')
def get_user(username):
    return {
        'Accept-Encoding': request.headers.get('Accept-Encoding'),
        'name': 'Antonio',
        'surname': 'Pérez',
        'username': escape(username),
        'id': 'A01273274',
        'age': 21
    }

@app.route('/users')
def get_users():
    return jsonify([
        {'id': 1, 'name': 'A'},
        {'id': 2, 'name': 'B'},
        {'id': 3, 'name': 'C'}
    ])
