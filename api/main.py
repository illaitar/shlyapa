import flask
import json 
from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    if flask.request.method == 'POST':
        message = 'Hello ' + flask.request.form['name-input'] + '!'
        import json
        with open('data.json', 'w') as f:
            json.dump({}, f)
    return flask.render_template('index.html', message=message)

