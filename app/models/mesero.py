from app import db

class Mesero(db.Model):
    __tablename__ = 'mesero'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
