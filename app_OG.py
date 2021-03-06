from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def default():
    return (os.environ.get('NAME', 'Name not configured'))


@app.route("/api")
def api():
    return jsonify(os.environ.get('TEST', 'Name not configured'))


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, port=port)
