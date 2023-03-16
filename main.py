from flask import Flask, render_template

# instanciando a classe Flask
app = Flask(__name__)


# decorator é uma função que começa com um @ 
# e sempre vem antes de uma função para atribuir uma nova funcionalidade à ela
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)