from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Aqui você pode implementar a lógica para enviar o e-mail ou salvar as informações em um banco de dados
        print(f"Nome: {name}, E-mail: {email}, Mensagem: {message}")
        
        return redirect(url_for('contact_success'))
    return render_template('contact.html')

@app.route('/contact/success')
def contact_success():
    return 'Obrigado pelo seu contato!'

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/about')
def about():
    return render_template('about.html')

#     pip install Flask-WTF

# Lucas Matheus Peres Morais
# 21:12
# pip install Flask-WTF[email]

# Lucas Matheus Peres Morais
# 21:12
# pip install Flask-FlashMessages

# Lucas Matheus Peres Morais
# 21:13
# pip install mysql-connector