from flask import Blueprint



dp = Blueprint('main', __name__)


from app.routes import informacion_routes, carrito_rutas, AgregrarAlCarrito, Faturas_routes
