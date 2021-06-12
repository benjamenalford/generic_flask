import socket
from bson import json_util
from flask import Flask, jsonify, render_template
import pymongo
import os
import json

# test

app = Flask(__name__)

h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)
print("Host Name is:" + h_name)
print("Computer IP Address is:" + IP_addres)
IP_addres2 = socket.gethostbyname(h_name)
print("public IP Address is:" + IP_addres2)
# setup mongo connection
serverUrl = os.environ.get('MONGO', "mongodb://localhost:27017")
client = pymongo.MongoClient(serverUrl)

# connect to mongo db (hoobastank) and collection (class)
db = client.hoobastank
class_collection = db.class_db


@app.route("/")
def default():
    return render_template('index.html')


@app.route("/api")
def api():
    data = class_collection.find()

    return json_util.dumps(data)


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, port=port)
