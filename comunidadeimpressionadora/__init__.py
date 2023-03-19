from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instanciando a classe Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b480e6cf1f889e49d122f1a7de513f84'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)

from comunidadeimpressionadora import routes