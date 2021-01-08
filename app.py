from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def default():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
    )


if __name__ == '__main__':
    app.run(debug=True)
