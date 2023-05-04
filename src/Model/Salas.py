from config.db import db, app, ma 

class Salas(db.Model):
    __tablename__ = "tblsalas"

    id = db.Column(db.Integer, primary_key=True)
    nombre_sala = db.Column(db.String(50))
    capacidad = db.Column(db.String(50))

    def __init__(self, nombre_sala, capacidad):
        self.nombre_sala = nombre_sala
        self.capacidad = capacidad
        
with app.app_context():
    db.create_all()

class SalasSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_salas','capacidad')