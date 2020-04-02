#!/usr/bin/env python

from bson import ObjectId
from flask import request, Flask
import json
from pymongo import MongoClient

# The unique ID field is a type that can't be serialized, so this
# custom JSON encoder turns it into a string and handles everything
# else the default way.
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# Unexplained: when running in the standalone test mode, this can be done
# once, and used in the handler functions. When running under WSGI, it
# needs to be done for every invocation. There's probably a way to optimize
# this, but I'm not really sure about the execution model.
def get_db():
    client = MongoClient('mongodb://db:27017/')
    return client.roomme

app = Flask(__name__)

@app.route('/')
def get_all():
    return 'iot-roomme!'

@app.route('/locations', methods=['POST'])
def create_new():
    try:
        new_location = request.get_json()
        id = get_db().locations.insert_one(new_location).inserted_id
        return 'request accepted (id {})'.format(id)
    except TypeError:
        print(request)
        return 'bad request', 400

@app.route('/locations')
def list_locations():
    all_locations = list(get_db().locations.find())
    return JSONEncoder().encode(all_locations)
        
@app.route('/locations/id/<id>')
def get_location(id):
    location = get_db().locations.find_one({"_id": ObjectId(id)})
    if location is None:
        return 'id {} not found'.format(id), 404
    else:
        return JSONEncoder().encode(location)

