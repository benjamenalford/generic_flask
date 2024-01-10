from flask import Flask, jsonify
from sqlalchemy import create_engine

app = Flask(__name__)

connection_string = "postgres:postgres@localhost:5432/customer_db"

@app.route("/")
def default():
    dict_list = [{'id':1,'source':'python'}]
    return jsonify(dict_list)

@app.route("/api")
def api():
    engine = create_engine(f'postgresql://{connection_string}')
    results = engine.execute("SELECT * FROM customer_name").fetchall()
    data = []
    index = 0
    for item in results:
        data.append({'id': results[index][0],
                     'firstname': results[index][1],
                     'lastname': results[index][2],
                     })
        index += 1
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5010)
