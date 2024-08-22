from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.plato import Plato
from app.models.carrito import Carrito
from app import db


bp = Blueprint('carritos', __name__)
carrito_compras = Carrito()

@bp.route('/ListarCarrito')
def listar():
    items = carrito_compras.getItems()
    return render_template('plato/list.html', items=items)

@bp.route('/ListarProductos')
def index():
    productos = carrito_compras
    return render_template('index.html', productos=productos)

@bp.route('/agregar/<int:id>', methods=['POST'])
def agregar_al_carrito(id):
    cantidad = int(request.form['cantidad'])
    carrito_compras.agregar_producto(id, cantidad)
    return redirect(url_for('plato.index'))
    #return "Entra a agregar corrito"

@bp.route('/eliminarc/<int:id>', methods=['GET', 'POST'])
def eliminar_del_carrito(id):
    carrito_compras.eliminar_producto(id)
    return redirect(url_for('carritos.listar'))


@bp.route('/realizar_compra')
def realizar_compra():
    total = carrito_compras.calcular_total()
    return render_template('carrito/realizar_compra.html', total=total)

@bp.route('/generar_factura', methods=['POST'])
def generar_factura():
    total = carrito_compras.calcular_total()
    # Aquí puedes almacenar la información en la base de datos (crear registros en Carrito y Factura)
    # y luego limpiar el carrito de compras
    carrito_compras.carrito = []
    return render_template('carrito/factura.html', total=total)

@bp.route('/itemscarrito', methods=['GET', 'POST'])
def tCarrito():
    a = carrito_compras.tamañoD()
    print("Entra a carrito rutas", a)
    return f"Entra a carrito {carrito_compras.tamañoD()}"