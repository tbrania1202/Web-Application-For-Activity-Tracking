from flask import Blueprint, render_template, request, redirect, url_for
from app.scraper import scrape_website
from app.messages_json import load_messages, add_message

home = Blueprint("home", __name__)

@home.route("/", methods=["GET", "POST"])
def home_page():
    scraped_text = scrape_website()
    
    if request.method == "POST":
        new_message = request.form.get("message", "").strip()
        if new_message:
            add_message(new_message)
        return redirect(url_for("home.home_page"))
    
    messages = load_messages()

    return render_template("home.html", scraped_text=scraped_text, messages=messages)
