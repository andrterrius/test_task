import random_generator

from users import users
from flask import Flask, render_template, request, flash
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key recruto'

@app.route('/random/', methods=['GET', 'POST'])
def random_nonauth():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and check_password_hash(users[username]['password'], password):
            return random_generator.code_generate()
        flash("Логин или пароль введены неверно", "danger")
    return render_template('login.html')

@app.route('/random/nonauth')
def nonauth_index():
    return random_generator.code_generate()

if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
