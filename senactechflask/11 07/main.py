from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, validators
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import logging
from contextlib import contextmanager
import io
from xlsxwriter import Workbook
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import make_response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@contextmanager
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pythonbas'
        )
        yield connection
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            criar_banco_de_dados()
            connection = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pythonbas'
            )
            yield connection
        else:
            logging.error(f"Erro de conexão com o banco de dados: {err}")
            raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def criar_banco_de_dados():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        cursor = connection.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS pythonbas;')
        cursor.execute('USE pythonbas;')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                mensagem TEXT NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_contatos (
                users_id INT NOT NULL,
                contatos_id INT NOT NULL,
                situacao VARCHAR(255) NOT NULL,
                PRIMARY KEY (contatos_id, users_id),
                FOREIGN KEY (users_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (contatos_id) REFERENCES contatos(id) ON DELETE CASCADE
            );
        ''')
        connection.commit()
    except mysql.connector.Error as err:
        logging.error(f"Erro ao criar o banco de dados ou tabelas: {err}")
        raise
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])
    mensagem = TextAreaField('Mensagem:', validators=[validators.DataRequired(), validators.Length(min=10)])

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[validators.DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired(), validators.Length(min=4, max=20)])
    password = PasswordField('Password:', validators=[
        validators.DataRequired(),
        validators.Length(min=8),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        email = form.email.data
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
                if cursor.fetchone() is not None:
                    return render_template('register.html', form=form, msg='Esse usuário já existe')
                cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)',
                               (username, password, email))
                connection.commit()
            return render_template('sucesso.html', message="Cadastro realizado com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao registrar usuário: {err}")
            return render_template('register.html', form=form, msg='Erro ao registrar usuário')
    return render_template('register.html', form=form)

@app.route('/sucesso')
def sucesso():
    message = request.args.get('message', 'Operação realizada com sucesso!')
    return render_template('sucesso.html', message=message)

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = FormularioContato()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        mensagem = form.mensagem.data
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor()
                sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
                values = (nome, email, mensagem)
                cursor.execute(sql, values)
                contato_id = cursor.lastrowid
                connection.commit()

                if 'loggedin' in session:
                    sql = "INSERT INTO user_contatos (users_id, contatos_id, situacao) VALUES (%s, %s, %s)"
                    values = (session['id'], contato_id, 'Enviado')
                    cursor.execute(sql, values)
                    connection.commit()

            return redirect('/sucesso')
        except mysql.connector.Error as err:
            logging.error(f"Erro ao salvar dados no banco de dados: {err}")
            mensagem_erro = "Ocorreu um erro ao processar o seu contato. Tente novamente mais tarde."
            return render_template('erro.html', mensagem_erro=mensagem_erro), 500
    return render_template('contato.html', form=form)

@app.route('/sucesso')
def sucesso():
    message = request.args.get('message', 'Operação realizada com sucesso!')
    return render_template('sucesso.html', message=message)

@app.route('/consultar', methods=['GET', 'POST'])
def consultar():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    form = FormularioContato()  # Add this line to create the form

    try:
        with get_db_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            if request.method == 'POST':
                busca = f"%{request.form.get('busca')}%"
                cursor.execute('''
                    SELECT c.id AS contatos_id, c.nome, c.email, c.mensagem, uc.situacao
                    FROM contatos c
                    JOIN user_contatos uc ON c.id = uc.contatos_id
                    WHERE uc.users_id = %s AND (c.nome LIKE %s OR c.email LIKE %s OR c.mensagem LIKE %s)
                    ORDER BY c.nome
                ''', (session['id'], busca, busca, busca))
            else:
                cursor.execute('''
                    SELECT c.id AS contatos_id, c.nome, c.email, c.mensagem, uc.situacao
                    FROM contatos c
                    JOIN user_contatos uc ON c.id = uc.contatos_id
                    WHERE uc.users_id = %s
                    ORDER BY c.nome
                ''', (session['id'],))
            user_contatos = cursor.fetchall()
        return render_template("consultar.html", user_contatos=user_contatos, form=form)
    except Exception as e:
        logging.error(f"Erro ao consultar dados: {e}")
        return render_template('erro.html', mensagem_erro=str(e)), 500

@app.route('/inserir', methods=['GET', 'POST'])
def inserir():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    form = FormularioContato()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        mensagem = form.mensagem.data
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor()
                sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
                values = (nome, email, mensagem)
                cursor.execute(sql, values)
                contato_id = cursor.lastrowid
                connection.commit()
                
                sql = "INSERT INTO user_contatos (users_id, contatos_id, situacao) VALUES (%s, %s, %s)"
                values = (session['id'], contato_id, 'Enviado')
                cursor.execute(sql, values)
                connection.commit()
                
            return redirect(url_for('visualizer'))
        except mysql.connector.Error as err:
            logging.error(f"Erro ao inserir dados: {err}")
            return render_template('erro.html', mensagem_erro="Erro ao inserir dados"), 500
    return render_template('inserir.html', form=form)

@app.route('/alterar/<int:id>', methods=['GET', 'POST'])
def alterar(id):
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    form = FormularioContato()
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            
            # Check if the message belongs to the logged-in user
            cursor.execute('SELECT * FROM user_contatos WHERE users_id = %s AND contatos_id = %s', (session['id'], id))
            if not cursor.fetchone():
                flash('Você não tem permissão para editar esta mensagem.', 'error')
                return redirect(url_for('visualizer'))
            
            if request.method == 'POST' and form.validate_on_submit():
                nome = form.nome.data
                email = form.email.data
                mensagem = form.mensagem.data
                sql = "UPDATE contatos SET nome=%s, email=%s, mensagem=%s WHERE id=%s"
                values = (nome, email, mensagem, id)
                cursor.execute(sql, values)
                connection.commit()
                flash('Mensagem atualizada com sucesso!', 'success')
                return redirect(url_for('visualizer'))
            else:
                cursor.execute('SELECT * FROM contatos WHERE id = %s', (id,))
                contato = cursor.fetchone()
                if contato:
                    form.nome.data = contato['nome']
                    form.email.data = contato['email']
                    form.mensagem.data = contato['mensagem']
                else:
                    flash('Mensagem não encontrada.', 'error')
                    return redirect(url_for('visualizer'))
    except mysql.connector.Error as err:
        logging.error(f"Erro ao alterar dados: {err}")
        flash('Ocorreu um erro ao alterar os dados. Por favor, tente novamente.', 'error')
        return redirect(url_for('visualizer'))
    
    return render_template('alterar.html', form=form, id=id)
@app.route('/excluir/<int:id>')
def excluir(id):
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM contatos WHERE id = %s', (id,))
            connection.commit()
        return redirect(url_for('visualizer'))
    except mysql.connector.Error as err:
        logging.error(f"Erro ao excluir dados: {err}")
        return render_template('erro.html', mensagem_erro="Erro ao excluir dados"), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
                user = cursor.fetchone()
                if user and check_password_hash(user['password'], password):
                    session['loggedin'] = True
                    session['id'] = user['id']
                    session['username'] = user['username']
                    return render_template('login.html', form=form, login_success=True)
                else:
                    return render_template('login.html', form=form, msg='Usuário ou senha incorretos')
        except mysql.connector.Error as err:
            logging.error(f"Erro ao fazer login: {err}")
            return render_template('erro.html', mensagem_erro="Erro ao processar o login"), 500
    return render_template('login.html', form=form)

@app.route('/visualizer')
def visualizer():
    if 'loggedin' in session:
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute('''
                    SELECT c.* 
                    FROM contatos c
                    JOIN user_contatos uc ON c.id = uc.contatos_id
                    WHERE uc.users_id = %s
                ''', (session['id'],))
                messages = cursor.fetchall()
            return render_template('visualizer.html', username=session['username'], messages=messages)
        except mysql.connector.Error as err:
            logging.error(f"Erro ao buscar mensagens: {err}")
            return render_template('erro.html', mensagem_erro="Erro ao buscar mensagens"), 500
    return redirect(url_for('login'))

@app.route('/relatorio_excel')
def gerar_relatorio_excel():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    try:
        with get_db_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
                SELECT c.*
                FROM contatos c
                JOIN user_contatos uc ON c.id = uc.contatos_id
                WHERE uc.users_id = %s
                ORDER BY c.id
            ''', (session['id'],))
            data = cursor.fetchall()

        # Criar um objeto de planilha do Excel em memória
        output = io.BytesIO()
        workbook = Workbook(output)
        worksheet = workbook.add_worksheet()

        # Definir o cabeçalho da planilha
        worksheet.write('A1', 'ID')
        worksheet.write('B1', 'Nome')
        worksheet.write('C1', 'Email')
        worksheet.write('D1', 'Mensagem')
        
        # Escrever os dados da tabela na planilha
        for i, row in enumerate(data):
            worksheet.write(i + 1, 0, row['id'])
            worksheet.write(i + 1, 1, row['nome'])
            worksheet.write(i + 1, 2, row['email'])
            worksheet.write(i + 1, 3, row['mensagem'])

        workbook.close()
        output.seek(0)

        # Criar a resposta HTTP com os cabeçalhos corretos
        response = make_response(output.getvalue())
        response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        response.headers['Content-Disposition'] = 'attachment; filename=relatorio_contatos.xlsx'

        return response

    except Exception as e:
        logging.error(f"Erro ao gerar relatório Excel: {e}")
        return render_template('erro.html', mensagem_erro="Erro ao gerar relatório Excel"), 500

@app.route('/relatorio_pdf')
def gerar_relatorio_pdf():
    if 'loggedin' not in session:
        return redirect(url_for('login'))

    try:
        with get_db_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('''
                SELECT c.*
                FROM contatos c
                JOIN user_contatos uc ON c.id = uc.contatos_id
                WHERE uc.users_id = %s
                ORDER BY c.id
            ''', (session['id'],))
            data = cursor.fetchall()

        # Criar um PDF
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.setTitle('Relatório de Contatos')

        # Definir o cabeçalho do relatório
        c.setFont('Helvetica-Bold', 14)
        c.drawString(50, 750, 'Relatório de Contatos')

        # Definir as colunas do relatório
        c.setFont('Helvetica-Bold', 12)
        c.drawString(50, 725, 'ID')
        c.drawString(100, 725, 'Nome')
        c.drawString(250, 725, 'Email')
        c.drawString(400, 725, 'Mensagem')

        # Escrever os dados da tabela no relatório
        c.setFont('Helvetica', 10)
        for i, row in enumerate(data):
            y = 700 - i * 20
            c.drawString(50, y, str(row['id']))
            c.drawString(100, y, str(row['nome']))
            c.drawString(250, y, str(row['email']))
            c.drawString(400, y, str(row['mensagem'])[:30] + '...' if len(row['mensagem']) > 30 else str(row['mensagem']))

        # Salvar o conteúdo do PDF no buffer
        c.save()

        # Obter o conteúdo do buffer como uma string
        pdf_content = buffer.getvalue()

        # Criar a resposta HTTP com os cabeçalhos corretos
        response = make_response(pdf_content)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=relatorio_contatos.pdf'

        return response

    except Exception as e:
        logging.error(f"Erro ao gerar relatório PDF: {e}")
        return render_template('erro.html', mensagem_erro="Erro ao gerar relatório PDF"), 500

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.errorhandler(Exception)
def erro_geral(erro):
    logging.error(f"Erro não tratado: {str(erro)}")
    return render_template('erro.html', mensagem_erro="Ocorreu um erro inesperado."), 500

if __name__ == '__main__':
    criar_banco_de_dados()
    app.run(debug=True)