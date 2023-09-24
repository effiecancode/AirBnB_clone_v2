#!/usr/bin/python3
"""Starts a Flask web application.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays a html page with a list of all states objects from dbstorgae
    sorted by name
    """
    states = storage.all("state")
    return render_template("7-states_list.html", states_list=states)

@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
