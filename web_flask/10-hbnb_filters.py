#!/usr/bin/python3
"""starts a Flask web application
Routes:
    /hbnb_filters: HBnB HTML filters page
"""
from models import storage
from models.amenity import Amenity
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """
    displays the main HBnB filters HTML page
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_session(exc):
    """End the current  session of SQLAlchemy"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
