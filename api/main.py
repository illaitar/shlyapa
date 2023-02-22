import flask
import json 
from flask import Flask
import os.path



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if os.path.isfile("/tmp/back.txt"):
        fo= open("/tmp/back.txt", "r")
        message = fo.readline()
        fo.close()
    else:
        message = ''
    if flask.request.method == 'POST':
        print("heyheyheyhey")
        # message = "!!"
        fo= open("/tmp/back.txt", "w")
        nm = str(flask.request.form['name-input'])
        filebuffer = [nm]
        fo.writelines(filebuffer)
        fo.close()

        # message = 'Hello ' + flask.request.form['name-input'] + '!'

    return flask.render_template('index.html', message=message)

