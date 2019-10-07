from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/spell_check')
def spell():
    return "Spell checker page"


if __name__ == '__main__':
    app.run()
