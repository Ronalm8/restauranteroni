from app import db

class Mesa(db.Model):
    __tablename__ = 'mesa'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)