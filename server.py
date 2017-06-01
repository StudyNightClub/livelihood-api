#!/bin/usr/env python3
# encoding: utf-8

from flask import Flask
from flask import request
app = Flask(__name__)

import json

@app.route('/')
def greet():
    return json.dumps({'greet': 'Hello there.'})

@app.route('/api')
def api():
    return json.dumps(request.args)
