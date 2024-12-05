from flask import Blueprint

# Crear el blueprint
hello_bp = Blueprint('hello', __name__)

# Ruta del "Hola Mundo"
@hello_bp.route('/')
def hello_world():
    return '¡Hola, Mundo!'
