from app import db

class Usuario (db.Model):
    __tablename__ ='usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    correo =db.Column(db.String(255), nullable=False)
    contraseña =db.Column(db.String(255), nullable=False)
    telefono =db.Column(db.String(45), nullable=False)
    dirreccion =db.Column(db.String(255), nullable=False)

