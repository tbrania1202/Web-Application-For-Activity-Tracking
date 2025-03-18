from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    from app.blueprints.home import home
    app.register_blueprint(home)

    return app