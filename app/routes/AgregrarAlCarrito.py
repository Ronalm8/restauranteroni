from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Usuario, Plato, Pedido, Mesero, Mesa, DetallePedido, carrito

from app import db

bp = Blueprint('Agregar_carritos', __name__)
carrito_compras = carrito.Carrito()

@bp.route('/ListarCarrito')
def listar():
    items = carrito_compras.getItems()
    return render_template('plato/list.html', items=items)

@bp.route('/AgregarAlCarrito', methods=['POST'])
def agregar_al_carrito():
    plato_id = request.form.get('plato_id')
    cantidad = request.form.get('cantidad', 1)

    plato = Plato.query.get(plato_id)
    if plato:
        carrito_compras.add_item(plato, cantidad)
        return redirect(url_for('carritos.listar'))
    else:
        return "Plato no encontrado", 404
