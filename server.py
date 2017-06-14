#!/bin/usr/env python3
# encoding: utf-8

import os
from datetime import datetime
from flask import Flask, request, json, send_file
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound

import dbconnector
from event import Event, Area, Coordinate

app = Flask(__name__)
VERSION = 'v3.0.0'

class EventsParameters(object):
    METADATA = 'metadata'
    TYPE = 'type'
    AFTER = 'after'
    BEFORE = 'before'
    CITY = 'city'
    DISTRICT = 'district'
    FIELDS = 'fields'
    IDS = 'ids'

SCHEMA_FILE = 'events.json'
with open(SCHEMA_FILE, 'r') as fin:
    SCHEMA = json.load(fin)

DB_URL = os.environ.get('LIVELIHOOD_DB')
if DB_URL:
    dbconnector.connect_to_db(DB_URL)
else:
    dbconnector.connect_to_inmemory_db()

@app.route('/')
def greet():
    return send_file('./static/usage.html')

@app.route('/events')
def show_events():
    metadata = request.args.get(EventsParameters.METADATA, 0, int)
    if metadata == 1:
        return json.jsonify(SCHEMA)

    session = dbconnector.Session()

    # The base of the query command
    query = session.query(Event).filter(Event.update_status == 'new')

    # "ids" parameter
    ids = request.args.get(EventsParameters.IDS)
    ids = split_csv(ids)
    if ids:
        query = query.filter(Event.id.in_(ids))

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

    # "after" parameter
    after = parse_date(request.args.get(EventsParameters.AFTER))
    if after:
        query = query.filter(Event.end_date > after)

    # "before" parameter
    before = parse_date(request.args.get(EventsParameters.BEFORE))
    if before:
        query = query.filter(Event.start_date < before)

    # "fields" parameter
    fields = get_fields()

    result = []
    for e in query:
        result.append(e.to_dict(fields))

    return json.jsonify(result)

@app.route('/events/<string:event_id>')
def show_single_event(event_id):
    session = dbconnector.Session()

    query = session.query(Event).filter(Event.id == event_id)
    fields = get_fields()

    try:
        event = query.one()
        return json.jsonify(event.to_dict(fields))
    except MultipleResultsFound:
        print('Multiple event with ID {}, this shouldn\'t happen.'.format(event_id))
    except NoResultFound:
        print('No event with ID {}.'.format(event_id))

    return ''


def get_event_types():
    types = request.args.get(EventsParameters.TYPE, None, str)
    if types == 'all':
        types = None
    return split_csv(types)


def get_fields():
    fields = request.args.get(EventsParameters.FIELDS)
    return split_csv(fields)


def split_csv(value):
    if value:
        return [t.lower() for t in value.split(',')]
    else:
        return None


def parse_date(date):
    if not date:
        return None

    try:
        return datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print('Invalid date format {}'.format(date))
        return None
