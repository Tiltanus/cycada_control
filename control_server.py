import time
from datetime import datetime

from flask import Flask, request, send_file

app = Flask(__name__)

@app.route("/")
def control():
    return send_file("./control.txt")

app.run()