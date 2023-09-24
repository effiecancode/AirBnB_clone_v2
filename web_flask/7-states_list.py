#!/usr/bin/python3
"""Starts a Flask web application.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays a html page with a list of all states objects from dbstorgae
    sorted by name
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_session(exc):
    """End the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
