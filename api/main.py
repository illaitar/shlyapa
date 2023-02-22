import flask
import json 
from flask import Flask
import os.path



app = Flask(__name__)

@app.route('/cards', methods=['GET', 'POST'])
def home():
    message = ''
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
        fo = open(f"/tmp/{code}.txt", "w")
        fo.writelines(current)
        fo.close()
        message = "Submitted Cards!"
        # message = 'Hello ' + flask.request.form['name-input'] + '!'

    return flask.render_template('index.html', message=message)

@app.route('/', methods=['GET', 'POST'])
def ma():
    return flask.render_template('main.html')
    
@app.route('/host', methods=['GET', 'POST'])
def host():
    code = ''
    entered_code = False
    if flask.request.method == 'POST':
        if flask.request.form["building"] == "manos":
            # gameCodeForm
            entered_code = True
            code = flask.request.form['code']
            fo = open(f"/tmp/{code}.txt", "w")
            fo.close()
            message = "Submitted Cards!"
        else:
            # readyForm
            return flask.redirect(flask.url_for('game'))
    return flask.render_template('host.html', gamecode=code,entered_code=entered_code)
    
    
@app.route('/game', methods=['GET', 'POST'])
def game():
    code="sosat"
    fo = open(f"/tmp/{code}.txt", "r")
    cards=fo.readlines()
    fo.close()
    cards = ','.join(cards)
    return flask.render_template('game.html', cards = cards)