from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def default():
    dict_list = [{'id':1,'source':'python'}]
    return jsonify(dict_list)

@app.route("/api")
def api():
    dict_list = [{'id':1,'source':'python'}]
    return jsonify(dict_list)

if __name__ == '__main__':
    app.run(debug=True, port=5010)
