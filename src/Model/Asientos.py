from config.db import db, app, ma 

class asientos(db.Model):
    __tablename__ = "tblasientos"

    id = db.Column(db.Integer, primary_key=True)
    id_sala = db.Column(db.Integer, db.ForeignKey('tblsalas.id'))
    numero = db.Column(db.Integer)
    estado = db.Column(db.String(50))
  

    def __init__(self, id_sala ,numero, estado):
        self.id_sala = id_sala
        self.numero = numero
        self.estado = estado
        
with app.app_context():
    db.create_all()

class asientosSchema(ma.Schema):
    class Meta:
        fields = ('id','id_sala','numero','estado')