from flask import Flask, jsonify
from sqlalchemy import create_engine
import os

app = Flask(__name__)

# your port is probably 5432 not 5433 like mine is here
connection_string = "postgres:postgres@localhost:5433/customer_db"


@app.route("/")
def default():
    #prints the environment variable NAME, if it exists
    return (os.environ.get('NAME', 'Name not configured'))


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


port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True, port=port)
