from flask import Flask, render_template, redirect, url_for, request
from models.db import db
from models.produto import Produto
import math

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

app = create_app()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manipular', methods=['GET'])
def pgManipular():
    PRODUTOS = Produto.query.all()
    return render_template('CRUD.html', produtos = PRODUTOS)

@app.route('/produtos',  methods=['GET'])
def produtos_paginados():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    start = (page-1)*per_page
    end = start + per_page
    PRODUTOS = Produto.query.all()
    total_pages = math.ceil(len(PRODUTOS)/per_page)

    produtos_da_pagina = PRODUTOS[start:end]

    return render_template('paginados.html', produtos = produtos_da_pagina, page = page, total_pages = total_pages )
    
@app.route('/adicionarProd', methods=['POST'])
def adicionarProd():
    nome = request.form.get('nome')
    preco = float(request.form.get('preco'))
    Produto.adicionar(nome, preco)
    return redirect(url_for('pgManipular'))

@app.route('/excluirProd/<int:id>', methods=['GET'])
def excluirProd(id):
    prod = Produto.query.get(id)
    prod.excluir()
    return redirect(url_for('pgManipular'))

@app.route('/alterarProd/<int:id>', methods=['POST'])
def alterarProd(id):
    prod = Produto.query.get(id)
    nome = request.form.get('nome', prod.nome)
    preco = float(request.form.get('preco', prod.preco))
    prod.alterar(nome, preco)
    return redirect(url_for('pgManipular'))

if __name__ == "__main__":
    app.run(debug=True)
