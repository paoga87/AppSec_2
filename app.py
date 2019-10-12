from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_sqlalchemy import SQLAlchemy

# Basic setups
basedir  = '127.0.0.1:5000'
db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'WxND4o83j4K4iO3762'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    twofa = db.Column(db.String(120))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        uname = request.form['uname']
        password = request.form['pword']
        twofa = request.form['2fa']

        register = user(username = uname, password = pword, twofa = twofa)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        uname = request.form.get['uname']
        password = request.form.get['pword']
        return redirect(url_for('spell'))
    return render_template("login.html")

@app.route('/spell_check')
def spell():
    return "Spell checker page"


if __name__ == '__main__':
    db.create_all()
    app.run()
