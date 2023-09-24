#!/usr/bin/python3
"""Starts Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Displays Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """
    Displays HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C(text):
    """
    Displays C
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_Python(text):
    """
    Displays Python
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """
    Displays n and checks if it's a number
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html(n):
    """
    Displays number html
    """
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
