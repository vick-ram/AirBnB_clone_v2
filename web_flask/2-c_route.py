#!/usr/bin/python3
"""Receive a path variable"""
from flask import Flask, redirect

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Hello function"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB funtion"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Function to return a text with passed variable"""
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
