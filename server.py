#!/bin/usr/env python3
# encoding: utf-8

import os
from flask import Flask, request, json
import dbconnector
from event import Event, Area, Coordinate

app = Flask(__name__)

class EventsParameters:
    METADATA = 'metadata'
    TYPE = 'type'
    AFTER = 'after'
    BEFORE = 'before'
    CITY = 'city'
    DISTRICT = 'district'
    FIELDS = 'fields'

SCHEMA_FILE = 'response_schema.json'
with open(SCHEMA_FILE, 'r') as fin:
    SCHEMA = json.load(fin)

db_location = os.environ.get('LIVELIHOOD_DB')
if db_location:
    dbconnector.connect_to_db(db_location)
else:
    dbconnector.connect_to_inmemory_db()

@app.route('/')
def greet():
    return json.jsonify({'greet': 'Hello there.'})

@app.route('/events')
def events():
    metadata = request.args.get(EventsParameters.METADATA, 0, int)
    if metadata == 1:
        return json.jsonify(SCHEMA)

    session = dbconnector.Session()

    event_type = request.args.get(EventsParameters.TYPE, "all", str)
    if event_type == 'all':
        types = ['Water', 'Power', 'Road']
    else:
        types = [t.title() for t in event_type.split(',')]

    result = []
    for e in session.query(Event).filter(Event.type.in_(types)):
        result.append(e.to_dict())

    return json.jsonify(result)

