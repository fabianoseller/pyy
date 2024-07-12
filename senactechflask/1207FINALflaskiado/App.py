from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, validators, SelectField
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

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
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            criar_banco_de_dados()
            return conecta_no_banco_de_dados()
        else:
            print("Erro de conexão com o banco de dados:", err)
            raise

# Função para criar o banco de dados e tabelas
def criar_banco_de_dados():
    # ... (código para criar o banco de dados e tabelas)

# Definição dos formulários
class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])
    mensagem = TextAreaField('Mensagem:', validators=[validators.DataRequired(), validators.Length(min=10)])

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[validators.DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])

class AtribuirContatoForm(FlaskForm):
    usuario = SelectField('Atribuir para:', coerce=int)

# Decorator para verificar login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'loggedin' not in session:
            flash('Por favor, faça login para acessar esta página.', 'warning')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

# Rotas
@app.route('/login', methods=['GET', 'POST'])
def login():
    # ... (código da função login)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # ... (código da função register)

@app.route('/', methods=['GET', 'POST'])
def contato():
    # ... (código da função contato)

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

@app.route('/consultar')
@login_required
def consultar():
    # ... (código da função consultar)

@app.route('/atribuir/<int:contato_id>', methods=['GET', 'POST'])
@login_required
def atribuir_contato(contato_id):
    # ... (código da função atribuir_contato)

@app.route('/atualizar_status/<int:contato_id>', methods=['POST'])
@login_required
def atualizar_status(contato_id):
    # ... (código da função atualizar_status)

@app.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))

@app.errorhandler(Exception)
def erro_geral(erro):
    mensagem_erro = str(erro)
    return render_template('erro.html', mensagem_erro=mensagem_erro), 500

if __name__ == '__main__':
    criar_banco_de_dados()
    app.run(debug=True)