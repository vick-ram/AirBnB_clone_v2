#!/usr/bin/python3
"""Receive a path variable"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """Hello function"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB funtion"""
    return “HBNB”


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun():
    """Function to return a text with passed variable"""
    return f"C {escape(text)}"