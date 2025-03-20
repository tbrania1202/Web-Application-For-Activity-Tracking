from flask import Blueprint, render_template
from app.scraper import scrape_website

home = Blueprint("home", __name__)

@home.route("/")
def home_page():
    scraped_text = scrape_website()
    return render_template("home.html", scraped_text=scraped_text)