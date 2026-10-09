import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    mensaje = "¡Bienvenido a mi sitio web creado con Python y Flask!"
    return render_template('index.html', titulo="Mi Página Web", mensaje=mensaje)

if __name__ == '__main__':
    # Lee el puerto asignado por el servidor (Render/Railway) o usa el puerto 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
