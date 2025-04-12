from flask import request
from datetime import datetime
from database import activity_collection

def filter_sort_activities():
    query = {}
    user = request.form.get("user_name")
    name = request.form.getlist("activity_name")
    activity_type = request.form.getlist("activity_type")
    intensity = request.form.getlist("activity_intensity")
    date_from = request.form.get("date_from")
    date_to = request.form.get("date_to")

    if user:
        query["user_id"] = user
    if name:
        query["name"] = {"$in": name}
    if activity_type:
        query["type"] = {"$in": activity_type}
    if intensity:
        query["intensity"] = {"$in": intensity}
    if date_from and date_to:
        try:
            date_from = datetime.strptime(date_from, "%Y-%m-%d").strftime("%Y-%m-%d")
            date_to = datetime.strptime(date_to, "%Y-%m-%d").strftime("%Y-%m-%d")
            query["date"] = {"$gte": date_from, "$lte": date_to}
        except:
            print("Invalid date format provided.")

    sort_by = request.form.get("sort_by")
    sort_order = request.form.get("sort_order")

    if sort_by and sort_order:
        if sort_order == "desc":
            sort_order = -1
        else:
            sort_order = 1
        activities = list(activity_collection.find(query).sort(sort_by, sort_order))
    else:
        activities = list(activity_collection.find(query))

    return activities