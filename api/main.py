import flask
import json 
from flask import Flask


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    fo= open("/tmp/back.txt", "r")
    message = fo.readline()
    fo.close()
    if flask.request.method == 'POST':
        print("heyheyheyhey")
        # message = "!!"
        fo= open("/tmp/back.txt", "r")
        filebuffer = [flask.request.form['name-input']]
        fo.writelines(filebuffer)
        fo.close()

        # message = 'Hello ' + flask.request.form['name-input'] + '!'

    return flask.render_template('index.html', message=message)

