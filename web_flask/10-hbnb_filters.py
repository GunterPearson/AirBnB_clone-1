#!/usr/bin/python3
""" states list flask """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(arg):
    """ tear down current session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    """ for hbnb_project """
    states = storage.all("State")
    return render_template("10-hbnb_filters.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
