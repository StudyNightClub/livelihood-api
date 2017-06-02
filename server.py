#!/bin/usr/env python3
# encoding: utf-8

from flask import Flask, request, json
app = Flask(__name__)

class EventsParameters:
    METADATA = 'metadata'

SCHEMA_FILE = 'response_schema.json'
with open(SCHEMA_FILE, 'r') as fin:
    SCHEMA = json.load(fin)

@app.route('/')
def greet():
    return json.jsonify({'greet': 'Hello there.'})

@app.route('/events')
def events():
    metadata = request.args.get(EventsParameters.METADATA, 0, int)
    if metadata == 1:
        return json.jsonify(SCHEMA)

    return json.jsonify(request.args)

