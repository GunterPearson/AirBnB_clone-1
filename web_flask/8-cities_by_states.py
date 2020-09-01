#!/usr/bin/python3
""" states list flask """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(arg):
    """ tear down current session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_city_list():
    """ render state list """
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
