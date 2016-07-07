from werkzeug.utils import secure_filename
import os
import sys
from flask import *
import json

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

app.run()
