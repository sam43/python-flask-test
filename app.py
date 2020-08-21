from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/auth')
def goto():
    return 'If you are an Admin, please login first'


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/<name>')
def welcomeUser(name):
    return f'Welcome, {name}'


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/admin')
def redirectUser():
    return redirect(url_for('welcomeUser', name='Admin!'))


if __name__ == '__main__':
    app.run()
