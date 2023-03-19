from main import app, database
from comunidadeimpressionadora.models import Usuario, Post

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username="Lira", email="lira@gmail.com", senha="123456")
#     database.session.add(usuario)
#     database.session.commit()

with app.app_context():
    meus_usuarios = Usuario.query.all()
    print(meus_usuarios[0].username)

# with app.app_context():
#      database.drop_all()
#      database.create_all()