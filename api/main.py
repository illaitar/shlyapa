import flask
import json 
from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    with open('data.json', 'r') as f:
        message = "TADAA"
    if flask.request.method == 'POST':
        print("heyheyheyhey")
        # message = "!!"
        message = 'Hello ' + flask.request.form['name-input'] + '!'

    return flask.render_template('index.html', message=message)

