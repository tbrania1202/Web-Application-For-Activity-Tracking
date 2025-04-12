from flask import Flask
import os
from dotenv import load_dotenv
from app.blueprints.home import home
from app.blueprints.add_activity import add_activity_bp
from app.blueprints.search_activity import search_activity_bp
from app.blueprints.statistics import statistics_bp
from app.blueprints.report import report_bp

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.register_blueprint(home)
    app.register_blueprint(add_activity_bp)
    app.register_blueprint(search_activity_bp)
    app.register_blueprint(statistics_bp)
    app.register_blueprint(report_bp)

    return app