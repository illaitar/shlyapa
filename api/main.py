import flask
import json 
from flask import Flask
import os.path
from random import shuffle
import numpy as np


app = Flask(__name__)
app.static_folder = 'static'

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
        message = "Карты отправлены!"
        # message = 'Hello ' + flask.request.form['name-input'] + '!'
        not_entered_cards = False
    return flask.render_template('index.html', message=message, not_entered_cards=not_entered_cards)


@app.route('/', methods=['GET', 'POST'])
def ma():
    print("hey!")
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
            code = flask.request.form['code2']
            return flask.redirect(flask.url_for('game', codex=code))
    return flask.render_template('host.html', gamecode=code,entered_code=entered_code,gamecode2=code)
    
    
@app.route('/game/<codex>', methods=['GET', 'POST'])
def game(codex):
    fo = open(f"/tmp/{codex}.txt", "r")
    cards=fo.readlines()
    fo.close()
    # cards2 = ' '.join(cards)
    render_start = True
    round_ended = False
    nextnum = 0
    cur_card = ''
    rd = ''
    if flask.request.method == 'POST':
        render_start = False
        if flask.request.form["state"] == "start":
            # start
            rd = list(np.arange(len(cards)))
            shuffle(rd)
            nextnum = 0
            cur_card = cards[rd[0]]
        elif flask.request.form["state"] == "next":
            if flask.request.form["posttype"] == "nxt":
                #next number
                nextnum = int(flask.request.form["num"])
                nextnum += 1
                if nextnum == len(cards):
                    render_start = True
                    pass
                else:
                    rd = flask.request.form["rd"][1:-1]
                    rd = [int(elem) for elem in rd.split(',')]
                    cur_card = cards[rd[nextnum]]
            else:
                # prev number
                nextnum = int(flask.request.form["num"]) - 1
                cur_card = "..."
                rd = flask.request.form["rd"][1:-1]
                rd = [int(elem) for elem in rd.split(',')]
                rd_part = rd[nextnum+1:]
                print(f"rd:{rd}, rd_part:{rd_part}")
                shuffle(rd_part)
                rd[nextnum+1:] = rd_part
        
    return flask.render_template('game.html', nextnum = nextnum, render_start = render_start, cur_card = cur_card, rd = rd)