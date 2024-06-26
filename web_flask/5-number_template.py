#!/usr/bin/python3
""" script that setup web app """
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ disply Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ disply HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def admin(text):
    """ Display 'C' followed by the value """
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def admin_py(text=None):
    """ display Python , followed by the value """
    if text:
        text = text.replace("_", " ")
        return f"Python {escape(text)}"
    else:
        return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """ return a number page """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temple(n):
    """ Function that display html page """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
