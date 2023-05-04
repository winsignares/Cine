from config.db import db, app, ma 

class Compras(db.Model):
    __tablename__ = "tblcompras"

    id  = db.Column(db.Integer, primary_key=True)
    id_usuarios  = db.Column(db.Integer, db.ForeignKey('tblusuarios.id'))
    id_funcion  = db.Column(db.Integer, db.ForeignKey('tblfuncion.id'))
    cantidad_tikets  = db.Column(db.Integer, primary_key=True)
    total_pagado = db.Column(db.String(50))
    fecha_compra  = db.Column(db.Integer, primary_key=True)

    def __init__(self, roles):
        self.roles = roles
        
with app.app_context():
    db.create_all()

class CompraSchema(ma.Schema):
    class Meta:
        fields = ('id','id_usuarios','id_funcion','cantidad_tikets','total_pagado','fecha_compra')