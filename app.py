# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask import render_template
from flask.ext import assets

app = Flask(__name__)
app.config.from_object(__name__)

env = assets.Environment(app)

# Tell flask-assets where to look for our coffeescript and sass files.
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


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/flow/<id>')
def show(id):
    return render_template('flow.html', flow_id=id)

if __name__ == '__main__':
    app.run(debug=True)
