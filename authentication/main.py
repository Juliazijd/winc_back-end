from cmd import PROMPT
import os
from click import prompt

from flask import Flask, flash, redirect, render_template, request, session, url_for
from isort import code
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)

@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        session['password'] = hash_password(session['password'])
        if session['password'] == get_users().get(session['username']):
            flash('You are successfully logged in')
            return redirect(url_for('dashboard', error=False))
        else:
            error = 'invalid username/password'
    return render_template('login.html', error=error)


@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html", title="Dashboard")


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('username', None)
    return redirect(url_for("index"))
