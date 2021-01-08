from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def default():
    return (os.environ.get('NAME', 'none'))


@app.route("/api")
def api():
    return jsonify("test")


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, port=port)
