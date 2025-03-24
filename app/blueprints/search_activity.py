from flask import Blueprint, render_template
from database import activity_collection

search_activity_bp = Blueprint('search_activity', __name__)

@search_activity_bp.route("/search_activity", methods=["GET", "POST"])
def search_activity_page():   
    activities = list(activity_collection.find())
    return render_template("search_activity.html", activities=activities)
