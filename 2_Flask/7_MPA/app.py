from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key='1234'

@app.route('/')
def carregarHome():
    return render_template('index.html')

@app.route('/paginaEspecifica', methods=['POST'])
def paginaEspecifica():
    page = request.form['page']
    match(page):
        case 'noticias':
            return render_template('noticias.html')
        case 'comics':
            return render_template('comics.html')
        case 'filmes':
            return render_template('filmes.html')
        case 'jogos':
            return render_template('jogos.html')
        case 'mais':
            return render_template('mais.html')
    
    #notícias, comics, filmes, jogos, mais

if __name__=='__main__':
    app.run(debug=True)
    
