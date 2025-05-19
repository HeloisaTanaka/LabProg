#from flask import render_template

#@app.route('/bemvindo/<nome>')
#def bemvindo(nome):
#    return render_template('bemvindo.html', usuario=nome)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bemvindo/<nome>')
def bemvindo(nome):
        return render_template('index.html', usuario=nome)

if __name__ == '__main__':
        app.run(debug=True)