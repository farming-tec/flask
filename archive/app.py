# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
# Evitar inyección de código
from markupsafe import escape 

app = Flask(__name__)
CORS(app)

# localhost:port/
@app.route('/')
def hello_world():
    return 'Hello Python!'

# localhost:port/
# Ruta estática -> Responde sólo a /hola
@app.route('/hola')
def hola():
    return 'Hola mundo'

# Rutas con parametros
# SQL y NoSQL DB
# DRY -> Don't repeat yourself
# Authentication vs Authorization
@app.route('/user/<username>')
def get_user(username):
    # Esto es un dictionary {} python
    # HashMap -> JSON -> 
    #       Tienen una 'key' y un 'value'
    # Dictionary -> Distintos 'types' de valores
    user = {
        'name': 'Antonio',
        'surname': 'Perez',
        'username': escape(username),
        'id': 'A01273274',
        'age': 21
    }

    # Return as JSON
    return user

@app.route('/users')
def get_users():
    return jsonify([
        {'id': 1, 'name': 'A'},
        {'id': 2, 'name': 'B'},
        {'id': 3, 'name': 'C'}
    ])

# @app.route('/user/<username>')
# def user(username):

#     return { 
#         'Accept-Encoding': request.headers.get('Accept-Encoding'),
#         'name': 'Antonio',
#         'username': escape(username),
#         'id': 'A01273274',
#         'age': 21
#     }