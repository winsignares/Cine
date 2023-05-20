from config.db import db, app, ma 


class Peliculas(db.Model):
    __tablename__ = "tblpeliculas"


    id  = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    genero = db.Column(db.String(200))
    duracion = db.Column(db.Time)
    sinopsis = db.Column(db.String(200))
    director = db.Column(db.String(200))
    img = db.Column(db.String(200))

    def __init__(self, titulo, genero, duracion, sinopsis, director, img):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.sinopsis = sinopsis
        self.director = director
        self.img = img


with app.app_context():
    db.create_all()

class peliculaSchema(ma.Schema):
    class Meta:
        fields = ('id','titulo','genero','duracion','sinopsis','director','img')