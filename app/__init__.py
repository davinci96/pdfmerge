from flask import Flask

# Config file
from .config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    return app
