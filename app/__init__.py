from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)


    from app.routes import informacion_routes, AgregrarAlCarrito, carrito_rutas,Faturas_routes
    app.register_blueprint(informacion_routes.bp)
    app.register_blueprint(carrito_rutas.bp)
    app.register_blueprint(AgregrarAlCarrito.bp)
    app.register_blueprint(Faturas_routes.bp)

 

    return app