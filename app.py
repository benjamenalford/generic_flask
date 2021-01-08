from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def default():
    return ("Available Routes:<br/>")


@app.route("/api")
def api():
    return jsonify("test")


if __name__ == '__main__':
    app.run(debug=True)
