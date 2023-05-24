from config.db import db, app, ma 

class compras(db.Model):
    __tablename__ = "tblcompras"

    id  = db.Column(db.Integer, primary_key=True)
    id_usuarios  = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_funcion  = db.Column(db.Integer, db.ForeignKey('tblfunciones.id'))
    cantidad_tickets  = db.Column(db.Integer)
    total_pagado = db.Column(db.Float)
    fecha_compra  = db.Column(db.Date)

    def __init__(self,  id_usuarios, id_funcion, cantidad_tickets, total_pagado, fecha_compra):
        self.id_usuarios = id_usuarios
        self.id_funcion = id_funcion
        self.cantidad_tickets = cantidad_tickets
        self.total_pagado = total_pagado
        self.fecha_compra = fecha_compra
        
with app.app_context():
    db.create_all()

class comprasSchema(ma.Schema):
    class Meta:
        fields = ('id','id_usuarios','id_funcion','cantidad_tickets','total_pagado','fecha_compra')