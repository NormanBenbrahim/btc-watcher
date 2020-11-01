#!/bin/env python
import datetime
from flask import Flask, render_template, make_response, jsonify
from alpha_vantage.timeseries import TimeSeries
from google.cloud import datastore

datastore_client = datastore.Client()

# use this : https://www.tutlinks.com/deploy-fastapi-app-on-google-cloud-platform/
# [END gae_python38_datastore_store_and_fetch_times]
app = Flask(__name__)


# [START gae_python38_datastore_store_and_fetch_times]
def store_time(dt):
    entity = datastore.Entity(key=datastore_client.key('visit'))
    entity.update({
        'timestamp': dt
    })

    datastore_client.put(entity)


def fetch_times(limit):
    query = datastore_client.query(kind='visit')
    query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times
# [END gae_python38_datastore_store_and_fetch_times]


# [START gae_python38_datastore_render_times]
@app.route('/')
def root():
    # Store the current access time in Datastore.
    store_time(datetime.datetime.now())

    # Fetch the most recent 10 access times from Datastore.
    times = fetch_times(10)

    return render_template(
        'index.html', times=times)
# [END gae_python38_datastore_render_times]

# price route
@app.route('/api/price', methods=['GET'])
def price_now():
    """
    Get MMMED current price
    """
    return make_response(jsonify({"current_price":1}))

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
