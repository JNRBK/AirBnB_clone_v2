#!/usr/bin/python3
"""Flask Module"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """function that returns a hello message"""
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def do_hbnb():
    """return a message belongs to this route"""
    return "HBNB"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
