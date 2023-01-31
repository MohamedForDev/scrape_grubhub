
import json

import traceback
from datetime import datetime, timedelta
from flask import request, jsonify

from grubhub_scraper.utils import scrape
from grubhub_scraper import app

import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from lxml.html import fromstring
import json
from openpyxl.workbook import Workbook
import time
from grubhub_scraper.utils import save_html_page,request_get,get_sellenium_driver,scrape
from flask_socketio import SocketIO, emit
@app.route("/scrape_Grubhub", methods=["GET"])
def  scrape_Grubhub():
    response=asyncio.run(scrape())

    response["Data"]=True
    response["message"]='the xls file is stored in the current path having name the restaurent name'
    return jsonify(response),200
