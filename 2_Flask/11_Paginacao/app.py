from flask import Flask, request, render_template, abort, jsonify
import math

app = Flask(__name__)

PRODUTOS = [
    {'id': 1, 'nome': 'notebook gamer X', 'preco': 5200.00},
    {'id': 2, 'nome': 'mouse sem fio', 'preco': 150.00},
    {'id': 3, 'nome': 'teclado mecânico RGB', 'preco': 350.00},
    {'id': 4, 'nome': 'monitor 27 polegadas', 'preco': 1800.00},
    {'id': 5, 'nome': 'headset gamer 7.1', 'preco': 420.00},
    {'id': 6, 'nome': 'webcam full HD', 'preco': 280.00},
    {'id': 7, 'nome': 'mousepad RGB', 'preco': 120.00},
    {'id': 8, 'nome': 'ssd 1TB NVMe', 'preco': 450.00},
    {'id': 9, 'nome': 'memória RAM 16GB', 'preco': 320.00},
    {'id': 10, 'nome': 'placa de vídeo RTX 4060', 'preco': 2800.00},
    {'id': 11, 'nome': 'gabinete gamer', 'preco': 380.00},
    {'id': 12, 'nome': 'fonte 750W 80Plus', 'preco': 520.00},
    {'id': 13, 'nome': 'cadeira gamer', 'preco': 1200.00},
    {'id': 14, 'nome': 'mesa para computador', 'preco': 650.00},
    {'id': 15, 'nome': 'hub USB 3.0', 'preco': 90.00},
    {'id': 16, 'nome': 'cooler para processador', 'preco': 180.00},
    {'id': 17, 'nome': 'impressora laser', 'preco': 890.00},
    {'id': 18, 'nome': 'tablet 10 polegadas', 'preco': 1500.00},
    {'id': 19, 'nome': 'smartphone flagship', 'preco': 3500.00},
    {'id': 20, 'nome': 'smartwatch esportivo', 'preco': 680.00}
]

@app.route('/produtos')
def listar_produtos():
    return render_template('produtos.html', produtos = PRODUTOS)

@app.route('/produtos-paginados')
def listas_produtos():
    page = request.args.get('page', 1, type=int)
    per_page = 5

    start = (page-1)*per_page
    end = start + per_page
    total_pages = math.ceil(len(PRODUTOS)/per_page)

    produtos_da_pagina = PRODUTOS[start:end]

    return render_template('produtos_paginados.html', produtos = produtos_da_pagina, page = page, total_pages = total_pages )

@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    produto_encontrado = None
    for produto in PRODUTOS:
        if produto['id'] == produto_id:
            produto_encontrado = produto
            break
    if produto_encontrado is None:
        abort(404)
    
    return render_template('detalhe_produto.html', produto = produto_encontrado)

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def pagina_proibida(error):
    return render_template('403.html'), 403

@app.errorhandler(401)
def pagina_nao_autorizada(error):
    return render_template('401.html'), 401

@app.route('/api/buscar-produto', methods=['POST'])
def buscar_produto():
    dados = request.get_json()
    nome_produto = dados.get('nome', '').lower()
    
    resultado = [p for p in PRODUTOS if nome_produto in p['nome'].lower()]
    return jsonify({'produtos_encontrados': resultado})

if __name__ = '__main__':
    app.run(debug=True)