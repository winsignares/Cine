from config.db import db, app, ma 

class salas(db.Model):
    __tablename__ = "tblsalas"

    id = db.Column(db.Integer, primary_key=True)
    nombre_sala = db.Column(db.String(3))
    capacidad = db.Column(db.Integer)

    def __init__(self, nombre_sala, capacidad):
        self.nombre_sala = nombre_sala
        self.capacidad = capacidad
        
with app.app_context():
    db.create_all()

class salasSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_salas','capacidad')