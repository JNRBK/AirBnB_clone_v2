#!/usr/bin/python3
"""Flask module"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello():
    """
    Display hello
    Return: Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Display hbnb
    Return: HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Display C + text
    Return: C is fun!
    """
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
