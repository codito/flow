# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask import render_template
from flask.ext import assets

from flask_peewee.db import Database
from flask_peewee.rest import RestAPI

import config

# Application configuration
DATABASE = {
    'name': 'flow.db',
    'engine': 'peewee.SqliteDatabase',
}
DEBUG = True

# Initialize flask and load configuration
app = Flask(__name__)
app.config.from_object(config.ProductionConfig)

db = None
api = None

# Tell flask-assets where to look for our coffeescript and sass files.
env = assets.Environment(app)

env.load_path = [
    os.path.join(os.path.dirname(__file__), 'bower_components'),
    os.path.join(os.path.dirname(__file__), 'static'),
]

env.register(
    'js_all',
    assets.Bundle(
        'jquery/dist/jquery.min.js',
        'bootstrap/dist/js/bootstrap.min.js',
        output='js_all.js'
    )
)

env.register(
    'css_all',
    assets.Bundle(
        'bootstrap/dist/css/bootstrap.min.css',
        'bootstrap/dist/css/bootstrap-theme.min.css',
        output='css_all.css'
    )
)

# TODO this could be removed once we've a bower package for mapjs
env.register(
    'js_map',
    assets.Bundle(
        'mapjs/color-0.4.1.min.js',
        'mapjs/jquery.hammer.min.js',
        'mapjs/jquery.hotkeys.js',
        'mapjs/jquery.mousewheel-3.1.3.js',
        'mapjs/kinetic-v4.5.4.js',
        'mapjs/underscore-1.4.4.js',
        'mapjs/mapjs-compiled.js',
        'mapjs/testtree.js',
        output='js_map.js'
    )
)


def initialize():
    global db, api

    db = Database(app)

    # Setup models
    import models
    models.setup()

    # Register REST api
    api = RestAPI(app)
    api.register(models.Flow)
    api.setup()


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/flow/<id>')
def show(id):
    return render_template('flow.html', flow_id=id)
