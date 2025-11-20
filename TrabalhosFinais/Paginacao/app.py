from flask import Flask, render_template, redirect, url_for, request
from models.db import db
from controllers.produto_controller import produtos_bp

#Páginas de erro
#MVC blueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()

app.secret_key = 'chave_secreta_autofacil'
app.register_blueprint(produtos_bp)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
