from config.db import db, app, ma 

class Tikets(db.Model):
    __tablename__ = "Tikets"

    id_tikets = db.Column(db.Integer, primary_key=True)
    id_compra = db.Column(db.Integer, primary_key=True)
    id_funcion = db.Column(db.Integer, primary_key=True)
    asiento = db.Column(db.String(50))
    fecha_emision = db.Column(db.Integer, primary_key=True)

    def __init__(self, Tikets):
        self.id_tikets = Tikets
        
with app.app_context():
    db.create_all()

class TiketsSchema(ma.Schema):
    class Meta:
        fields = ('id_tikets','id_compra','id_funcion','asiento','fecha_emision')