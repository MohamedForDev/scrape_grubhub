from flask import Blueprint

app = Blueprint("grubhub_scraper API", __name__)

import grubhub_scraper.views
