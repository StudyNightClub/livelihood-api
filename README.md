# Livelihood API

API server for our livelihood data.

Currently it's just a dummy.

## Requirements

* Python 3
* Flask >= 0.12

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
`http://127.0.0.1:5000/api` to get recent livelihood events.

| Path   | Description       |
| ------ | ------------------|
| `/`    | Greeting message. |
| `/api` | Get livelihood events in JSON format. |

When calling `/api` without parameters, the event of all types from this date
will be returned.
You can use several parameters on `/api` for more specific results.

| Parameter | Acceptable Values | Description | Example |
| --------- | ----------------- | ----------- | ------- |
| type | `water`, `power`, and/or `road`. Comma separated. | The type of events you wish to query. If not specified, all types are used. | `/api?type=water,power` |
| start | Date in `YYYYMMDD` | If specified, events that ends before this date will be filtered out. If not specified, the current date will be used. | `/api?start=20170601` |
| end | Data in `YYYYMMDD` | If specified, events that starts after this date will be filtered out. | `/api?end=20170602` |
