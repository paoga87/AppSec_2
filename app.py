from flask import Flask
app = flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/register')
def register():
    return "Registration page"

@app.route('/login')
def login():
    return "Login page"

if __name__ == '__main__':
    app.run()
