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
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                        states=states, amenities=amenities)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['ENV'] = 'development'
    app.config['TESTING'] = True
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
