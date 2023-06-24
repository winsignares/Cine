from config.db import db, app, ma 

class asientos(db.Model):
    __tablename__ = "tblasientos"

    id = db.Column(db.Integer, primary_key=True)
    id_sala = db.Column(db.Integer, db.ForeignKey('tblsalas.id'))
    id_funcion = db.Column(db.Integer, db.ForeignKey('tblfunciones.id'))
    numero = db.Column(db.String(3))
    estado = db.Column(db.String(50))
  

    def __init__(self, id_sala,id_funcion ,numero, estado):
        self.id_sala = id_sala
        self.id_funcion = id_funcion
        self.numero = numero
        self.estado = estado
        
with app.app_context():
    db.create_all()

class asientosSchema(ma.Schema):
    class Meta:
        fields = ('id','id_sala','id_funcion','numero','estado')