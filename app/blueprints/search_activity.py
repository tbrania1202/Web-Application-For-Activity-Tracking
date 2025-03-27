from flask import Blueprint, render_template, request, redirect, url_for
from database import activity_collection
from bson.objectid import ObjectId
from datetime import datetime
from data.defined_data import ACTIVITY_TYPES

search_activity_bp = Blueprint('search_activity', __name__)


@search_activity_bp.route("/search_activity", methods=["GET", "POST"])
def search_activity_page():   
    activities = list(activity_collection.find())
    return render_template("search_activity.html", activities=activities)


@search_activity_bp.route("/edit_activity/<activity_id>", methods=["GET", "POST"])
def edit_activity(activity_id):
    activity = activity_collection.find_one({"_id": ObjectId(activity_id)})

    if request.method == "POST":
        activity_type = request.form.get("activity_type")
        date = request.form.get("activity_date")
        duration = request.form.get("activity_duration")
        metric_value = request.form.get("activity_metric")
        intensity = request.form.get("activity_intensity")
        notes = request.form.get("activity_notes")

        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%d-%m-%Y")
        try:
            metric_value = float(metric_value)
        except:
            metric_value = int(metric_value)

        updated_data = {
            "user_id": activity["user_id"],
            "name": activity["name"],
            "type": activity_type,
            "date": date,
            "duration": int(duration),
            "metric_name": activity["metric_name"],
            "metric_value": metric_value,
            "intensity": intensity,
            "notes": notes,
        }
        activity_collection.update_one({"_id": ObjectId(activity_id)}, {"$set": updated_data})
        return redirect(url_for("search_activity.search_activity_page"))

    return render_template("edit_activity.html", activity=activity, activity_types=ACTIVITY_TYPES)


@search_activity_bp.route("/delete_activity/<activity_id>", methods=["POST"])
def delete_activity(activity_id):
    activity_collection.delete_one({"_id": ObjectId(activity_id)})
    return redirect(url_for("search_activity.search_activity_page"))

