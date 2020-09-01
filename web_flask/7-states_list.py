#!/usr/bin/python3
""" states list flask """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(arg):
    """ tear down current session"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """ render state list """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
