from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from database import activity_collection

add_activity_bp = Blueprint('add_activity', __name__)

@add_activity_bp.route("/add_activity", methods=["GET", "POST"])
def add_activity_page():
    if request.method == "POST":
        user = request.form.get("user_name")
        name = request.form.get("activity_name")
        activity_type = request.form.get("activity_type")
        date = request.form.get("activity_date")
        duration = request.form.get("activity_duration")
        metric = request.form.get("activity_metric")
        intensity = request.form.get("activity_intensity")
        notes = request.form.get("activity_notes")

        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%d-%m-%Y")

        new_activity = {
            "user_id": user,
            "name": name,
            "type": activity_type,
            "date": date,
            "duration": int(duration),
            "metric": int(metric),
            "intensity": intensity,
            "notes": notes,
        }
        activity_collection.insert_one(new_activity)

        if activity_collection.count_documents({}) > 1000:
            oldest_activity = activity_collection.find().sort("date", 1).limit(1)
            activity_collection.delete_one({"_id": oldest_activity[0]["_id"]})

        return redirect(url_for('home.home_page'))

    return render_template("add_activity.html")
