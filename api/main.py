import flask
import json 
from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    fo= open("test.txt", "w")
    filebuffer = ["brave new world"]
    fo.writelines(filebuffer)
    fo.close()
    message = ''
    with open('data.json', 'r') as f:
        message = "TADAA"
    if flask.request.method == 'POST':
        print("heyheyheyhey")
        # message = "!!"
        message = 'Hello ' + flask.request.form['name-input'] + '!'

    return flask.render_template('index.html', message=message)

