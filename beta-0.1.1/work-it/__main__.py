from werkzeug.utils import secure_filename
import os
import sys
from flask import *
import json

def main():
    source = open("log.txt")
    log_file = source.readlines()
    num_size = sum(1 for line in log_file)
    data = [x for x in range(num_size)]
    date = [x for x in range(num_size)]
    temp = [x for x in range(num_size)]
    umid = [x for x in range(num_size)]

    for i in range(len(data)):
        data[i] = log_file[i]

    for i in range(len(data)):
        date[i] = (data[i][(data[i].index(':'))+1: data[i].index(';')])
        temp[i] = float(data[i][(data[i].index(':', data[i].index(':')+1)+1): data[i].index(';', data[i].index(';')+1)])
        umid[i] = float(data[i][(data[i].index('d', data[i].index('d')+2)+2): (len(data[i])-2)])

    for i in range(len(data)):
        print (date[i] == date[i])
        print (temp[i] == temp[i])
        print (umid[i] == umid[i])

    final_data = [x for x in range(num_size)]

    for i in range(len(data)):
        final_data[i] = {
            "date": date[i],
            "temp": temp[i],
            "umid": umid[i]
        }

    final_countdown = [final_data]

    with open("static/dumbster.json", "w") as f:
        for i in range(len(final_countdown)):
            json.dump(final_countdown[i], f)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/table?initial=A&final=B")
def table():
    return render_template("table.html")

@app.errorhandler(404)
def error404():
    return render_template("404.html")

if __name__ == "__main__":
    main()
    app.run()
