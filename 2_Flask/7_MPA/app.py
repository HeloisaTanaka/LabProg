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
        case 'cadastro':
            return render_template('cadastro.html')
        case 'eventos':
            return render_template('eventos.html')
        case 'login':
            return render_template('login.html')
        case 'premiações':
            return render_template('premiações.html')
    


if __name__=='__main__':
    app.run(debug=True)
    
