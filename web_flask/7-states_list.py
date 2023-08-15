#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def Hello_HBNB():
    """"""
    return render_template("7-states_list.html",
                           stt=storage.all("State").values())


@app.teardown_appcontext
def teardown(q):
    """"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
