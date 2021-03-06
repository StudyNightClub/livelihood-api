# Livelihood API v4.0.1

API server for our livelihood data.

## Requirements

* Flask 0.12
* SqlAlchemy 1.1
* enum34 1.1 (for python2 only)
* pymysql 0.7 (if using MySQL as database)

```
$ pip install -r requirements.txt
```

## Run

For development, you can host the API server on your own machine.

    $ export FLASK_APP=server.py
    $ export LIVELIHOOD_DB=<your_db_url>
    $ flask run
      * Running on http://127.0.0.1:5000

Note that your should replace `<your_db_url>` with real value. For example:
`sqlite:///livelihood.db`. If `LIVELIHOOD_DB` variable isn't set, the server
will use an empty in-memory DB as substitute.

Now the server should be hosted on http://127.0.0.1:5000
(might be slightly different depending on your environment).

Use the URL shown in the "Running on" line as the base URL for API.

## Usage

### Greet

    $ curl -X GET <api_url>/

A greeting message and version of the current engine will be returned.

### Get events

    $ curl -X GET <api_url>/events

A list of events will be returned in a JSON array of [this schema](response_schema.json).

There's several parameters for getting more specific results.

Parameter | Acceptable Values | Description | Example
--------- | ----------------- | ----------- | -------
`metadata` | `0` or `1` | If `metadata=1`, the response schema will be returned instead of the actual events, and the rest of the parameters will be ignored. Default: `0`. | `/events?metadata=1`
`type` | `water`, `power`, `road`, and `all`. Comma separated. | The type of events you wish to query. Default: `all`. | `/events?type=water,power`
`after` | Date in `YYYY-MM-DD` | Events that ends before this date will be filtered out. Default: current date.| `/events?after=2017-06-01`
`before` | Date in `YYYY-MM-DD` | If specified, events that starts after this date will be filtered out. | `/events?before=2017-06-02`
`city` | City name | If specified, only the events of the city will be returned. | `/events?city=臺北市`
`district` | District name | If specified, only the events of the district will be returned. | `/events?city=臺北市&district=大安區`
`fields` | Any field name of the event, comma separated. | If specified, only the corresponding fields will be returned. Note that the `id` field will always be returned. | `/events?fields=type,start_date,end_date`
`ids` | Event IDs, comma separated. | Only consider event(s) with specified ID(s). | `/events?ids=aaa,bbb`

### Get single event

    $ curl -X GET <api_url>/events/<event_id>

An event of the provided ID will be returned. If the ID doesn't match any
event, an empty string will be returned.

The `fields` parameter described above is still available.
