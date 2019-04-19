# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, redirect, flash, sessions
from game import Game

app = Flask(__name__)
app.secret_key = '15ec32122a441f3a34c92b8f22c2504e'

two_dots = Game('Two dots', 'Puzzle', 'Mobile')
tetris = Game('Tetris', 'Puzzle', 'Mobile')
sonic = Game('Sonic', 'Adventure', 'Mega drive')
quack_shot = Game('Quack shot', 'Adventure', 'NES')
list_of_games = [two_dots, tetris, sonic, quack_shot]

page_title = 'My list of favorites games'


@app.route('/')
def index():
    return render_template('index.html', title=page_title, games=list_of_games)


@app.route('/add')
def add():
    page_title = 'New Game'
    return render_template('form.html', title=page_title)


@app.route('/create', methods=['POST', ])
def create():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    if not name and not category:
        flash('Required fields are missing', 'error')
        return redirect('add')

    new_game = Game(name, category, console)
    list_of_games.append(new_game)
    return redirect('/')


if os.getenv('DEVELOP'):
    app.run(port=8080, debug=True)
else:
    app.run()
