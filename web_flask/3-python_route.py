#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """Display ""Hello HBNB" on /."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display “HBNB” /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space ).
    """
    return "C_{}".format(text).replace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """
    Display “Python ” followed by the value of the text variable
    (replace underscore _ symbols with a space).
    The default value of text is “is cool”.
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
