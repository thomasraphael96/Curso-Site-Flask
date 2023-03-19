from flask import render_template, url_for, request, flash, redirect
from comunidadeimpressionadora.forms import FormLogin, FormCriarConta
from comunidadeimpressionadora import app, database, bcrypt
from comunidadeimpressionadora.models import Usuario

lista_usuarios = ['Thomas','Evelyn','Marcus','Johnny']

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
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        #criando usuário dentro do banco de dados
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()

        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    
    return render_template('login.html', form_login = form_login, form_criarconta = form_criarconta)
