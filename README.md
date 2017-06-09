# Livelihood API v1.0.1

API server for our livelihood data.

## Requirements

* Python 3
* Flask 0.12
* SqlAlchemy 1.1
* gunicorn 19.7.1

```
$ pip3 install flask sqlalchemy
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

Add the following path to the base URL for API.

For example, with the local API server described above, use
`http://127.0.0.1:5000/events` to get recent livelihood events.

Path   | Description
------ | -----------
`/`    | Greeting message.
`/events` | Get livelihood events in JSON format.
`/events/<event_id>` | Get single livelihood event in JSON format.

There're several parameters for `/events` you can use to get more specific results.

Parameter | Acceptable Values | Description | Example
--------- | ----------------- | ----------- | -------
`metadata` | `0` or `1` | If `metadata=1`, the response schema will be returned instead of the actual events, and the rest of the parameters will be ignored. Default: `0`. | `/events?metadata=1`
`type` | `water`, `power`, `road`, and `all`. Comma separated. | The type of events you wish to query. Default: `all`. | `/events?type=water,power`
`after` | Date in `YYYY-MM-DD` | Events that ends before this date will be filtered out. Default: current date.| `/events?after=2017-06-01`
`before` | Date in `YYYY-MM-DD` | If specified, events that starts after this date will be filtered out. | `/events?before=2017-06-02`
`city` | City name | If specified, only the events of the city will be returned. | `/events?city=臺北市`
`district` | District name | If specified, only the events of the district will be returned. | `/events?city=臺北市&district=大安區`
`fields` | Any field name of the event, comma separated. | If specified, only the corresponding fields will be returned. Note that the `id` field will always be returned. | `/events?fields=type,start_date,end_date`

For single event, only the `fields` parameter is available.

The result will be a JSON of [this schema](response_schema.json).
