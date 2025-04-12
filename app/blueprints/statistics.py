from flask import Blueprint, render_template

statistics_bp = Blueprint("statistics", __name__)


@statistics_bp.route("/statistics", methods=["GET", "POST"])
def statistics_page():
    return render_template("statistics.html")