from app import db
from datetime import datetime

class Pedido(db.Model):
    __tablename__='pedido'
    id = db.Column(db.Integer, primary_key=True)
    FechaHora = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    mesa_id = db.Column(db.Integer, db.ForeignKey('mesa.id'))
    mesero_id = db.Column(db.Integer, db.ForeignKey('mesero.id'))
    


