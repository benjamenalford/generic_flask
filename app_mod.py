from bson import json_util
from flask import Flask, jsonify
import pymongo
import os
import json

app = Flask(__name__)

serverUrl = os.environ.get('MONGO', "mongodb://localhost:27017")
client = pymongo.MongoClient(serverUrl)

# connect to mongo db (hoobastank) and collection (class)
db = client.hoobastank
class_collection = db.class_db


@app.route("/")
def default():
    return (os.environ.get('NAME', 'Name not configured'))


@app.route("/api")
def api():
    data = class_collection.find()

    return json_util.dumps(data)


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, port=port)
