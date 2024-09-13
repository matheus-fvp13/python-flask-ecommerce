from flask import Flask
from src.routes import register_routes
from src.db import db

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_routes(app)
    db.init_app(app)
    return app