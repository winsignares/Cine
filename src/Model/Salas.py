from config.db import db, app, ma 

class Salas(db.Model):
    __tablename__ = "tblsalas"

    id = db.Column(db.Integer, primary_key=True)
    Nombre_sala = db.Column(db.String(50))
    Capacidad = db.Column(db.String(50))

    def __init__(self, Salas):
        self.id_salas = Salas
        
with app.app_context():
    db.create_all()

class SalasSchema(ma.Schema):
    class Meta:
        fields = ('id','Nombre_salas','Capacidad')