from flask import Flask

# Importamos el blueprint del archivo hello.py
from .hello import hello_bp

def create_app():
    # Crear la aplicación Flask
    app = Flask(__name__)
    
    # Registrar el blueprint
    app.register_blueprint(hello_bp)

    return app