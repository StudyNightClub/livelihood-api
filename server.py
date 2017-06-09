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

    # The base of the query command
    query = session.query(Event)

    # "type" parameter
    types = get_event_types()
    if types:
        query = query.filter(Event.type.in_(types))

    # "city" parameter
    city = request.args.get(EventsParameters.CITY)
    if city:
        query = query.filter(Event.city == city)

    # "district" parameter
    district = request.args.get(EventsParameters.DISTRICT)
    if district:
        query = query.filter(Event.district == district)

    result = []
    for e in query:
        result.append(e.to_dict())

    return json.jsonify(result)

def get_event_types():
    event_type = request.args.get(EventsParameters.TYPE, "all", str)
    if event_type == 'all':
        types = None
    else:
        types = [t.title() for t in event_type.split(',')]
    return types
