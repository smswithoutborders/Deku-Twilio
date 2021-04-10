#!/bin/python

import configparser
import requests

CONFIGS = configparser.ConfigParser(interpolation=None)

CONFIGS.read("config.ini")
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

    try:
        router_url = CONFIGS["CLOUD_API"]["url"]
        print(f"[+] Router url: {router_url}")
        api_request=requests.post(f"{router_url}/messages", json={"text":Body, "phonenumber":From})
    except Exception as error:
        print( error )
    else:
        print( api_request.text )
    
    return api_request.text



if CONFIGS["API"]["DEBUG"] == "1":
    # Allows server reload once code changes
    app.debug = True

app.run(host=CONFIGS["API"]["HOST"], port=CONFIGS["API"]["PORT"], debug=app.debug )
