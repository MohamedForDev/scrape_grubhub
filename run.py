from flask import Flask ,g
from grubhub_scraper import app as grubhub_scraper_app
app = Flask(__name__)


app.register_blueprint(grubhub_scraper_app)

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run(host='127.0.0.1', port=5000)
