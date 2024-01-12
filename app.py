#!/usr/bin/env python3
from flask import Flask, render_template, request,json,jsonify
import pandas as pd
from sklearn.cluster import KMeans

app = Flask(__name__)

#preload the model and train the data
data_file_path = 'notebooks/pokemon.csv'
data_df = pd.read_csv(data_file_path)
data_df = data_df.loc[data_df['base_experience'] >0 ]
filtered_df = data_df[data_df.describe().columns.to_numpy()]
y = filtered_df['type_0_id']
X = filtered_df[['stat_hp', 'stat_attack','stat_defense', 'stat_special-attack', 'stat_special-defense','stat_speed']]
model= KMeans(n_clusters=5)
model.fit(X)

@app.route("/")
def default():
    return render_template('index.html')

@app.route("/home")
def home():
    dict_list = [{'id':1,'source':'python'}]
    heading_text = "this text came from a varaible python"
    return render_template('home.html', data=dict_list, heading=heading_text)

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/api")
def api():
    dict_list = [{'id':1,'source':'python'}]
    return jsonify(dict_list)

@app.route('/get_data', methods=['POST'])
def get_data():
    if request.method == 'POST':
        data = request.form['data']
        # do something with the data
        print(data)
        return data

#Knn
@app.route("/knn")
def knn_route():
    return render_template('knn.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.form['data']
        #convert the data to json
        data = json.loads(data)
        print(data)
        #predict
        prediction =model.predict([data['data']])
        print(prediction[0])
        #return the prediction as an object
        return {'prediction': f'{prediction[0]}'}

if __name__ == '__main__':
    app.run(debug=True, port=5010)