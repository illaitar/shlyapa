import flask
import json 
from flask import Flask
import os.path
from random import shuffle


app = Flask(__name__)


@app.route('/cards', methods=['GET', 'POST'])
def home():
    message = ''
    not_entered_cards = True
    if flask.request.method == 'POST':
        code = flask.request.form['code']
        cards = [flask.request.form[f"card{i}"] for i in range(1,6)]
        cards = [card + '\n' for card in cards]
        current = []
        if os.path.isfile(f"/tmp/{code}.txt"):
            fo = open(f"/tmp/{code}.txt", "r")
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
        not_entered_cards = False
    return flask.render_template('index.html', message=message, not_entered_cards=not_entered_cards)


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
            code = flask.request.form['code']
            return flask.redirect(flask.url_for('game'), code=code)
    return flask.render_template('host.html', gamecode=code,entered_code=entered_code)
    
    
@app.route('/game/<code>', methods=['GET', 'POST'])
def game(code):
    code="sosat"
    fo = open(f"/tmp/{code}.txt", "r")
    cards=fo.readlines()
    fo.close()
    cards = ' '.join(cards)
    return flask.render_template('game.html', cards = cards)