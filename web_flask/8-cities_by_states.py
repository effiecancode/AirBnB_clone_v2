#!/usr/bin/python3
"""Starts a Flask web application.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities
"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities.
    sorted by name.
    """
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_session(exc):
    """End the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
