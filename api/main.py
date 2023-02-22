import flask
import json 
from flask import Flask
import os.path



app = Flask(__name__)

@app.route('/cards', methods=['GET', 'POST'])
def home():
    if flask.request.method == 'POST':
        code = flask.request.form['code']
        cards = [flask.request.form[f"card{i}"] for i in range(1,6)]
        current = []
        if os.path.isfile(f"/tmp/{code}.txt"):
            fo = open("/tmp/back.txt", "r")
            current = fo.readlines()
            fo.close()
        for card in cards:
            current.append(card)
        

        # message = "!!"
        fo = open("/tmp/back.txt", "w")
        fo.writelines(current)
        fo.close()
        message = "Submitted Cards!"
        # message = 'Hello ' + flask.request.form['name-input'] + '!'

    return flask.render_template('index.html', message="")

