from flask import Blueprint, request
from http import HTTPStatus

api = Blueprint('users', __name__)

@api.route('', methods=['GET'])
def get_users():
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    return users, HTTPStatus.OK

@api.route('', methods=['POST'])
def create_user():
    data = request.get_json()
    return {"message": "User created"}, HTTPStatus.CREATED
