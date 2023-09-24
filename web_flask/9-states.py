#!/usr/bin/python3
"""starts a Flask web app
Routes:
    /states: HTML page with a list of all State objects
    /states/<id>: HTML page displaying the given state with id
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """displays an HTML page with a list of all States
    sorted by name
    """
    states = storage.all(State)
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """displays an HTML page with info about id, if it exists"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown_session(exc):
    """End the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
