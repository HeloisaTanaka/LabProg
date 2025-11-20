from flask import Flask, Blueprint, render_template, redirect, url_for, request
from models.produto import Produto
import math

produtos_bp = Blueprint('produtos_bp', __name__)


@produtos_bp.route('/manipular', methods=['GET'])
def pgManipular():
    PRODUTOS = Produto.query.all()
    return render_template('CRUD.html', produtos = PRODUTOS)

@produtos_bp.route('/produtos',  methods=['GET'])
def produtos_paginados():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    start = (page-1)*per_page
    end = start + per_page
    PRODUTOS = Produto.query.all()
    total_pages = math.ceil(len(PRODUTOS)/per_page)

    produtos_da_pagina = PRODUTOS[start:end]

    return render_template('paginados.html', produtos = produtos_da_pagina, page = page, total_pages = total_pages )
    
@produtos_bp.route('/adicionarProd', methods=['POST'])
def adicionarProd():
    nome = request.form.get('nome')
    preco = float(request.form.get('preco'))
    Produto.adicionar(nome, preco)
    return redirect(url_for('produtos_bp.pgManipular'))

@produtos_bp.route('/excluirProd/<int:id>', methods=['GET'])
def excluirProd(id):
    prod = Produto.query.get(id)
    prod.excluir()
    return redirect(url_for('produtos_bp.pgManipular'))

@produtos_bp.route('/alterarProd/<int:id>', methods=['POST'])
def alterarProd(id):
    prod = Produto.query.get(id)
    nome = request.form.get('nome', prod.nome)
    preco = float(request.form.get('preco', prod.preco))
    prod.alterar(nome, preco)
    return redirect(url_for('produtos_bp.pgManipular'))

@produtos_bp.route('/detalhes/<int:id>')
def detalhes(id):
    return render_template('infoProd.html', produto = Produto.query.get(id))