from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bemvindo/<nome>')
def bemvindo(nome):
        # A variável nome assume o valor colocado na URL após o /bemvindo
        return render_template('index.html', usuario=nome)

if __name__ == '__main__':
        app.run(debug=True)

# render_template recarrega a página, podendo atribuir valores às tag do HTML
    # A tag usuario no HTML recebe o valor da variável nome do python
    # usuario=nome  --->  usuarioHTML = nomePython
    # ATENÇÃO: para fazer a integração, os arquivos .html devem ser armazenados na pasta 'templates'