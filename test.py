import json,urllib,ast

from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Woolworths"
