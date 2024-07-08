from flask import Flask, render_template, request, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
import mysql.connector
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'

# Função para conectar ao banco de dados
def conecta_no_banco_de_dados():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pythonbas'
        )
        return conexao
    except mysql.connector.Error as err:
        print("Erro de conexão com o banco de dados:", err)
        return None

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[validators.DataRequired()])

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        conexao = conecta_no_banco_de_dados()
        if conexao:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            user = cursor.fetchone()
            if user and check_password_hash(user['password'], password):
                session['loggedin'] = True
                session['id'] = user['id']
                session['username'] = user['username']
                return redirect(url_for('listar_usuarios'))
            else:
                return render_template('login.html', form=form, msg='Usuário ou senha incorretos')
    return render_template('login.html', form=form)

@app.route('/listar_usuarios')
def listar_usuarios():
    if 'loggedin' in session:
        conexao = conecta_no_banco_de_dados()
        if conexao:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute('SELECT id, username, email FROM users')
            usuarios = cursor.fetchall()
            conexao.close()
            return render_template('listar_usuarios.html', usuarios=usuarios)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
