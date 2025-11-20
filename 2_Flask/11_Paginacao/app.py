from flask import Flask, request, render_template, abort, jsonify
from models.Produto import Produto
from models.Produtos import Produtos
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

PRODUTOS = Produtos()

p1 = Produto(1, 'notebook gamer X', 5200.00)
p2 = Produto(2, 'mouse sem fio', 220.00)
p3 = Produto(3, 'teclado mecânico RGB', 150.00)
p4 = Produto(4, 'monitor 27 polegadas', 350.00)
p5 = Produto(5, 'headset gamer 7.1', 1800.00)
p6 = Produto(6, 'webcam full HD', 420.00)
p7 = Produto(7, 'mousepad RGB', 280.00)
p8 = Produto(8, 'ssd 1TB NVMe', 120.00)
p9 = Produto(9, 'memória RAM 16GB', 450.00)
p10 = Produto(10, 'placa de vídeo RTX 4060', 320.00)
p11 = Produto(11, 'gabinete gamer', 2800.00)
p12 = Produto(12, 'fonte 750W 80Plus', 380.00)
p13 = Produto(13, 'cadeira gamer', 1200.00)
p14 = Produto(14, 'mesa para computador', 650.00)
p15 = Produto(15, 'hub USB 3.0', 90.00)
p16 = Produto(16, 'cooler para processador', 180.00)
p17 = Produto(17, 'impressora laser', 890.00)
p18 = Produto(18, 'tablet 10 polegadas', 1500.00)
p19 = Produto(19, 'smartphone flagship', 3500.00)
p20 = Produto(20, 'smartwatch esportivo', 680.00)

itens = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]

for item in itens:
    PRODUTOS.adicionar(item)


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
    produto_encontrado = PRODUTOS.getProd(produto_id)
    if produto_encontrado == False:
        abort(404)
    return render_template('detalhe_produto.html', produto = produto_encontrado)

"""@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def pagina_proibida(error):
    return render_template('403.html'), 403

@app.errorhandler(401)
def pagina_nao_autorizada(error):
    return render_template('401.html'), 401"""

@app.route('/api/buscar-produto', methods=['POST'])
def buscar_produto():
    dados = request.get_json()
    nome_produto = dados.get('nome', '').lower()
    
    resultado = [p for p in PRODUTOS if nome_produto in p.nome.lower()]
    return jsonify({'produtos_encontrados': resultado})

@app.route('/manipular')
def manipular():
    return render_template('manipular.html')


if __name__ == '__main__':
    app.run(debug=True)