#!/bin/python

import configparser
import cloudfunctions
import routerfunctions

from platforms import Platforms

CONFIGS = configparser.ConfigParser(interpolation=None)

CONFIGS.read("config.router.ini")
# from ldatastore import Datastore

from flask import Flask, request, jsonify
app = Flask(__name__)

#datastore = Datastore(configs_filepath="libs/config.ini")
# datastore.get_datastore()
# datastore = Datastore(config=CONFIGS)

@app.route('/twilio_messages', methods=['POST', 'GET'])
def incoming_messages():
    From=request.values.get('From', None)
    To=request.values.get('To', None)
    FromCountry=request.values.get('FromCountry', None)
    NumSegments=request.values.get('NumSegments', None)
    Body=request.values.get('Body',None)

    print(f"From: {From}\nTo: {To}\nBody: {Body}\nFromCountry: {FromCountry}\nNumSegments: {NumSegments}")

    
    return Body



if CONFIGS["API"]["DEBUG"] == "1":
    # Allows server reload once code changes
    app.debug = True

app.run(host=CONFIGS["API"]["HOST"], port=CONFIGS["API"]["PORT"], debug=app.debug )
