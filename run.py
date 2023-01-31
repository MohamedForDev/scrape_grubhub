from flask import Flask ,g
from grubhub_scraper import app as chat_bot_ap
app = Flask(__name__)


app.register_blueprint(chat_bot_ap)

if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run(host='127.0.0.1', port=5000)
