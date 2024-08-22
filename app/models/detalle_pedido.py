from app import db

class DetallePedido(db.Model):
    __tablename__ = 'detallePedido'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), nullable=False)
    plato_id = db.Column(db.Integer, db.ForeignKey('plato.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Numeric(10, 2), nullable=False)

    