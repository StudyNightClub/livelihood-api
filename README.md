# Livelihood API

API server for our livelihood data.

Currently it's just a dummy.

## Requirements

* Python 3
* Flask 0.12
* SqlAlchemy 1.1

## Run

For development, you can host the API server on your own machine.

    $ export FLASK_APP=server.py
    $ flask run
      * Running on http://127.0.0.1:5000

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

There're several parameters for `/events` you can use to get more specific results.

Parameter | Acceptable Values | Description | Example
--------- | ----------------- | ----------- | -------
`metadata` | `0` or `1` | If `metadata=1`, the response schema will be returned instead of the actual events, and the rest of the parameters will be ignored. Default: `0`. | `events?metadata=1`
`type` | `water`, `power`, and/or `road`. Comma separated. | The type of events you wish to query. Default: `water,power,road`. | `/events?type=water,power`
`after` | Date in `YYYY-MM-DD` | Events that ends before this date will be filtered out. Default: current date.| `/events?after=2017-06-01`
`before` | Date in `YYYY-MM-DD` | If specified, events that starts after this date will be filtered out. | `/events?before=2017-06-02`
`city` | City name | If specified, only the events of the city will be returned. | `/events?city=臺北市`
`district` | District name | If specified, only the events of the district will be returned. | `/events?city=臺北市&district=大安區`
`fields` | Any field name of the event, comma separated. | If specified, only the corresponding fields will be returned. | `/events?fields=type,startDate,endDate`

The result will be a JSON of [this schema](response_schema.json).
