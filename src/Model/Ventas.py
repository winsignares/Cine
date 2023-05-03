from config.db import db, app, ma 

class Ventas(db.Model):
    __tablename__ = "Ventas"

    id_ventas = db.Column(db.Integer, primary_key=True)
    id_funcion = db.Column(db.Integer, primary_key=True)
    fecha_venta = db.Column(db.String(50))
    cantidad_tikets = db.Column(db.String(50))
    precio_total = db.Column(db.Integer, primary_key=True)
    
    def __init__(self, Ventas):
        self.id_ventas = Ventas
        
with app.app_context():
    db.create_all()

class VentasSchema(ma.Schema):
    class Meta:
        fields = ('id_venta','fecha_venta','cantidad_tikets','precio_total')