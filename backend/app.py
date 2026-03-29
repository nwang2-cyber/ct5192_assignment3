import logging
import os
from flask import Flask

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

NEW_RELIC_APP_NAME = os.getenv("NEW_RELIC_APP_NAME", "ct5192-backend")
NEW_RELIC_LICENSE_KEY = os.getenv("NEW_RELIC_LICENSE_KEY", "")

@app.before_request
def log_request():
    app.logger.info(f"New Relic app={NEW_RELIC_APP_NAME} received a request")

@app.route("/")
def home():
    app.logger.info("Backend homepage was visited")
    if NEW_RELIC_LICENSE_KEY:
        app.logger.info("NEW_RELIC_LOG backend root endpoint")
    return "Hello from backend"

@app.route("/health")
def health():
    app.logger.info("Backend health endpoint was checked")
    if NEW_RELIC_LICENSE_KEY:
        app.logger.info("NEW_RELIC_LOG backend health endpoint")
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)