#!/usr/bin/env python3
from flask import Flask, render_template, request,session,json,jsonify

app = Flask(__name__)

@app.route("/")
def default():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/api")
def api():
    return jsonify([{'id':1,'source':'python'}])

@app.route('/get_data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        data = request.form['data']
        # do something with the data
        print(data)
        return data

if __name__ == '__main__':
    app.run(debug=True, port=5010)