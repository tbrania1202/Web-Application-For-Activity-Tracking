from flask import Blueprint, jsonify

home = Blueprint("home", __name__)

@home.route("/")
def home_page():
    return jsonify({"message": "Welcome to the Home Page!"})