# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request, redirect, flash, session, url_for
from game import Game

app = Flask(__name__)
app.secret_key = '15ec32122a441f3a34c92b8f22c2504e'

two_dots = Game('Two dots', 'Puzzle', 'Mobile')
quack_shot = Game('Quack shot', 'Adventure', 'NES')
list_of_games = [two_dots, quack_shot]


@app.route('/')
def index():
    if is_not_authenticated():
        return redirect(url_for('login'))

    page_title = 'Your favorite games list'
    return render_template('index.html', title=page_title, games=list_of_games)


@app.route('/add')
def add():
    if is_not_authenticated():
        return redirect(url_for('login'))

    page_title = 'New Game'
    return render_template('form.html', title=page_title)


@app.route('/create', methods=['POST', ])
def create():
    if is_not_authenticated():
        return redirect(url_for('login'))

    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    if not name and not category:
        flash('Required fields are missing', 'warn')
        return redirect(url_for('add'))

    new_game = Game(name, category, console)
    list_of_games.append(new_game)

    flash(f'New game {name} success added', 'success')

    return redirect(url_for('index'))


@app.route('/login')
def login():
    page_title = 'Login'
    return render_template('login.html', title=page_title)


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash(f'Logout success!', 'success')
    return redirect(url_for('login'))


@app.route('/auth', methods=['POST'])
def auth():
    username = request.form['username']
    password = request.form['password']

    if password == 'admin' and not username == '':
        session['logged_user'] = username
        flash(f'Welcome {username}!', 'success')
        return redirect(url_for('index'))
    else:
        flash('Authentication fail, user or password are missing', 'error')
        return redirect(url_for('login'))


def is_not_authenticated() -> bool:
    return 'logged_user' not in session or session['logged_user'] is None


if __name__ == '__main__':
    if os.getenv('DEVELOP'):
        app.run(port=8080, debug=True)
    else:
        app.run()
