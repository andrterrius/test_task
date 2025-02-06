import random_generator

from users import users
from flask import Flask, render_template, request, flash, session, redirect, url_for
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key recruto'

@app.after_request
def preprocess(response):
    response.headers['location'] = request.referrer
    return response


@app.route('/random/', methods=['GET', 'POST'])
def random():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('random'))
        flash("Логин или пароль введены неверно", "danger")
    else:
        if session.get("username"):
            session.clear()
            return random_generator.code_generate()
    return render_template('login.html')

@app.route('/random/nonauth')
def random_nonauth():
    return random_generator.code_generate()

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
