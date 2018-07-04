# -*- encoding: utf-8 -*-
"""
Python Routes
Licence: GPLv3
"""

from app import app
from flask_restful import Api
from flask import jsonify
from .controller import *

api = Api(app)

api.add_resource(HomeApp, '/')
api.add_resource(GraphApp, '/graph')

@app.errorhandler(404)
def error(e):
    return jsonify({'error': 'Resource not found'}), 404
