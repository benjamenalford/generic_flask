from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def default():
    return ("text from flask")


@app.route("/api")
def api():
    return jsonify(os.environ.get('TEST', 'Name not configured'))

if __name__ == '__main__':
    app.run(debug=True, port=5010)
