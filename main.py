from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola, esta es una aplicación Flask desplegada en la nube!'
