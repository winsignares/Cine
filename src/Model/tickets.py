from config.db import db, app, ma 

class tickets(db.Model):
    __tablename__ = "tbltickets"

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_compra = db.Column(db.Integer, db.ForeignKey('tblcompras.id'))
    id_funcion = db.Column(db.Integer, db.ForeignKey('tblfunciones.id'))
    id_asiento = db.Column(db.Integer, db.ForeignKey('tblasientos.id'))
    fecha_emision = db.Column(db.Date)

    def __init__(self, id_compra, id_funcion, id_asiento, fecha_emision):
        self.id_compra = id_compra
        self.id_funcion = id_funcion
        self.id_asiento = id_asiento
        self.fecha_emision = fecha_emision
        
with app.app_context():
    db.create_all()

class ticketsSchema(ma.Schema):
    class Meta:
        fields = ('id','id_compra','id_funcion','id_asiento','fecha_emision')