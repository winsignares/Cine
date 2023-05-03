from config.db import db, app, ma 

class Funciones(db.Model):
    __tablename__ = "Funciones"

    id_funcion  = db.Column(db.Integer, primary_key=True)
    id_peliculas  = db.Column(db.Integer, primary_key=True)
    id_sala  = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(50))
    precio = db.Column(db.Integer, primary_key=True)

    def __init__(self, roles):
        self.roles = roles
        
with app.app_context():
    db.create_all()

class Funciones(ma.Schema):
    class Meta:
        fields = ('id_funcion','id_peliculas','id_sala','fecha','precio')