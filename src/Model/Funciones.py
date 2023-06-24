from config.db import db, app, ma 

class funciones(db.Model):
    __tablename__ = "tblfunciones" 

    id  = db.Column(db.Integer, primary_key=True)
    id_peliculas  = db.Column(db.Integer, db.ForeignKey('tblpeliculas.id'))
    id_sala  = db.Column(db.Integer, db.ForeignKey('tblsalas.id'))
    fecha = db.Column(db.Date)
    precio = db.Column(db.Integer)

    pelicula = db.relationship('peliculas', backref='funciones')
    sala = db.relationship('salas', backref='funciones')

    def __init__(self, id_peliculas, id_sala, fecha, precio):
        self.id_peliculas = id_peliculas
        self.id_sala = id_sala
        self.fecha = fecha
        self.precio = precio
        
        
with app.app_context():
    db.create_all()

class funcionesSchema(ma.Schema):
    class Meta:
        fields = ('id','id_peliculas','id_sala','fecha','precio')