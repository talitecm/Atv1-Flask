from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contato')
def formulario():
    return render_template('contato.html')

@app.route('/sucess')
def sucesso():
    return render_template('sucess.html')