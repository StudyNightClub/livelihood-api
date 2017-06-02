#!/bin/usr/env python3
# encoding: utf-8

from flask import Flask, request, json
app = Flask(__name__)

@app.route('/')
def greet():
    return json.jsonify({'greet': 'Hello there.'})

@app.route('/events')
def events():
    return json.jsonify(request.args)
