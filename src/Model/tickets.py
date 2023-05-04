from config.db import db, app, ma 

class Tickets(db.Model):
    __tablename__ = "tbltickets"

    id = db.Column(db.Integer, primary_key=True)
    id_compra = db.Column(db.Integer, db.ForeignKey('tblcompras.id'))
    id_funcion = db.Column(db.Integer, db.ForeignKey('tblfunciones.id'))
    asiento = db.Column(db.String(50))
    fecha_emision = db.Column(db.Integer, primary_key=True)

    def __init__(self, id_compra, id_funcion, asiento, fecha_emision):
        self.id_compra = id_compra
        self.id_funcion = id_funcion
        self.asiento = asiento
        self.fecha_emision = fecha_emision
        
with app.app_context():
    db.create_all()

class TicketsSchema(ma.Schema):
    class Meta:
        fields = ('id','id_compra','id_funcion','asiento','fecha_emision')