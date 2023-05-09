from config.db import db, app, ma 

class asientos(db.Model):
    __tablename__ = "tblasientos"

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    estado = db.Column(db.String(50))
  

    def __init__(self, numero, estado):
        self.numero = numero
        self.estado = estado
        
with app.app_context():
    db.create_all()

class asientosSchema(ma.Schema):
    class Meta:
        fields = ('id','numero','estado')