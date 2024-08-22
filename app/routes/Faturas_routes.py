from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.pedido import Pedido
from app.models.detalle_pedido import DetallePedido
from app.routes.carrito_rutas import carrito_compras
from app import db

bp = Blueprint('factura', __name__)

@bp.route('/factura')
def index():
    data = Pedido.query.all()
    return render_template('factura/index.html', data=data)
 

@bp.route('/addfactura', methods=['GET', 'POST'])
def add():
    factura = Pedido(fechafactura="Hoy", idcliente=1)
    db.session.add(factura)
    db.session.commit()
    print("factura id  ", factura.idfactura)
    return redirect(url_for('factura.addDetalle',id=factura.idfactura))

@bp.route('/adddetalle/<int:id>', methods=['GET', 'POST'])  
def addDetalle(id):  
    for item in carrito_compras.getItems():
        idproducto = item["producto"].idproducto
        cantidad = item["cantidad"]               
        detallepedido = DetallePedido(idfactura=id,idproducto=idproducto, cantidad=cantidad)
        db.session.add(detallepedido)
        db.session.commit() 
    carrito_compras.vaciarcarrito()
    return redirect(url_for('producto.index'))

@bp.route('/factura/<int:id>', methods=['GET', 'POST'])
def detalle(id):
    factura = Pedido.query.get_or_404(id)
    detalle = factura.productos
    return render_template('detalle/index.html', data=detalle, factura=factura)



@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    book = Pedido.query.get_or_404(id)

    if request.method == 'POST':
        #return "entra al if"
        book.titulo = request.form['titulo']
        book.author = request.form['author']
        
        db.session.commit()
        
        return redirect(url_for('book.index'))

    return render_template('books/edit.html', book=book)

@bp.route('/delete/<int:id>')
def delete(id):
    book = Pedido.query.get_or_404(id)
    
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('Book.index'))
