from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def load():
    return render_template('base.html')

@app.route('/paginaEspecifica', methods=['POST'])
def pagina_especifica():
    return render_template('pagina_especifica.html')

if __name__=='__main__':
    app.run(debug=True)