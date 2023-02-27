from flask import Flask

# commands:
# $env:FLASK_app='main.py'
# flask --app main.py run

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route("/contact/")
def contact():
    return "contact information"


@app.route("/calculate/7/9/")
def calculate():
    return str(7**9)