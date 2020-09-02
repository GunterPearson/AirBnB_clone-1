#!/usr/bin/python3
""" states list flask """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(arg):
    """ tear down current session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_id_list(id=None):
    """ render state list """
    states = storage.all("State")
    if id is not None:
        id = "State." + id
    return render_template('9-states.html', states=states, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
