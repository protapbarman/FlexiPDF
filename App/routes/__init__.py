from flask import Blueprint
from .pdf import pdf
from .main import main

# Register all blueprints here
blueprints = [pdf, main]

def register_blueprints(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
