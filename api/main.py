import flask
import json 
from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    if flask.request.method == 'POST':
        print("heyheyheyhey")
        # message = "!!"
        message = 'Hello ' + flask.request.form['name-input'] + '!'
        with open('data.json', 'w') as f:
            message = "TADAA"
    return flask.render_template('index.html', message=message)

