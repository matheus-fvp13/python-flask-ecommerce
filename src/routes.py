from flask import Blueprint, jsonify, request
from http import HTTPStatus
from src.controllers import user_controller

API_PREFIX = '/api/v1'

def register_routes(app):
    app.register_blueprint(user_controller.api, url_prefix=f'{API_PREFIX}/users')