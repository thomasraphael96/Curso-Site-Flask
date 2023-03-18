from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta

# instanciando a classe Flask
app = Flask(__name__)

lista_usuarios = ['Thomas','Evelyn','Marcus','Johnny']

app.config['SECRET_KEY'] = 'b480e6cf1f889e49d122f1a7de513f84'

# decorator é uma função que começa com um @ 
# e sempre vem antes de uma função para atribuir uma nova funcionalidade à ela
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

# liberar o método POST para ser possível enviar informações para o site (utilizado nos forms). Ele vem bloqueado por segurança
# método GET já vem liberado por padrão
@app.route('/login', methods=['GET','POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        #fez login com sucesso
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        #criou conta com sucesso
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login = form_login, form_criarconta = form_criarconta)

if __name__ == '__main__':
    app.run(debug=True)