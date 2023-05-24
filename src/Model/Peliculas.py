from config.db import db, app, ma 

class peliculas(db.Model):
    __tablename__ = "tblpeliculas"

    id  = db.Column(db.Integer, primary_key=True)
    titulo  = db.Column(db.String(50))
    genero  = db.Column(db.String(50))
    duracion = db.Column(db.String(50))
    sinopsis = db.Column(db.Text())
    director = db.Column(db.String(50))
    imagen = db.Column(db.String(100))

    def __init__(self, titulo, genero, duracion, sinopsis, director,imagen):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.sinopsis = sinopsis
        self.director = director
        self.imagen = imagen
        
with app.app_context():
    db.create_all()

class peliculasSchema(ma.Schema):
    class Meta:
        fields = ('id','titulo','genero','duracion','sinopsis','director','imagen')