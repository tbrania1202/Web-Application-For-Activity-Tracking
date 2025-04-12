from flask import Blueprint, render_template, url_for, request
from database import activity_collection
from app.filter_sort_wrapper import filter_sort_activities
from data.defined_data import ACTIVITY_NAMES, ACTIVITY_TYPES

statistics_bp = Blueprint("statistics", __name__)


@statistics_bp.route("/statistics", methods=["GET", "POST"])
def statistics_page():
    query = {}
    activities = list(activity_collection.find(query))
    
    if request.method == "POST":
        activities = filter_sort_activities()
    
    return render_template("statistics.html", activities=activities, form_action=url_for('statistics.statistics_page'),
                           activity_names=ACTIVITY_NAMES, activity_types=ACTIVITY_TYPES)