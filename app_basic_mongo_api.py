from bson import json_util
from flask import Flask, jsonify
import pymongo
import json

app = Flask(__name__)

serverUrl = "mongodb://localhost:27017"
client = pymongo.MongoClient(serverUrl)

# connect to mongo db (hoobastank) and collection (class)
db = client.hoobastank
class_collection = db.class_db

@app.route("/")
def default():
    return ("text from flask")

@app.route("/api")
def api():
    data = class_collection.find()
    return json_util.dumps(data)

if __name__ == '__main__':
    app.run(debug=True, port=5010)
