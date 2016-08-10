from werkzeug.utils import secure_filename
import os
import sys
from flask import *
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.errorhandler(404)
def error404():
    return render_template("404.html")

app.run()
