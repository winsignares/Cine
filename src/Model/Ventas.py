from config.db import db, app, ma 

class Ventas(db.Model):
    __tablename__ = "tblventas"

    id = db.Column(db.Integer, primary_key=True)
    id_funcion = db.Column(db.Integer, db.ForeignKey('tblfunciones.id'))
    fecha_venta = db.Column(db.String(50))
    cantidad_tikets = db.Column(db.String(50))
    precio_total = db.Column(db.Integer, primary_key=True)
    
    def __init__(self, id_funcion, fecha_venta, cantidad_tikets, precio_total):
        self.id_funcion = id_funcion
        self.fecha_venta = fecha_venta
        self.cantidad_tikets = cantidad_tikets
        self.precio_total = precio_total
        
with app.app_context():
    db.create_all()

class VentasSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha_venta','cantidad_tikets','precio_total')