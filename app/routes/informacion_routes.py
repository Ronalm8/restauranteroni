from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models import Usuario, Plato, Pedido, Mesero, Mesa, DetallePedido, carrito
from app.routes.carrito_rutas import carrito_compras

from app import db

bp = Blueprint('plato', __name__)

@bp.route('/')
def index():
    data = Plato.query.all()
    return render_template('plato/index.html', data=data, t=carrito_compras.tamañoD())

@bp.route('/plato/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        # Agrega otros campos del plato según tu modelo
        new_plato = Plato(nombre=nombre)  # Completa con otros campos
        db.session.add(new_plato)
        db.session.commit()
        return redirect(url_for('plato.index'))

    return render_template('carrito/factura.html')

@bp.route('/plato/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    plato = Plato.query.get_or_404(id)

    if request.method == 'POST':
        plato.nombre = request.form['nombre']
        # Actualiza otros campos del plato según tu modelo
        db.session.commit()
        return redirect(url_for('plato.index'))

    return render_template('plato/edit.html', plato=plato)

@bp.route('/plato/delete/<int:id>')
def delete(id):
    plato = Plato.query.get_or_404(id)
    db.session.delete(plato)
    db.session.commit()
    return redirect(url_for('plato.index'))