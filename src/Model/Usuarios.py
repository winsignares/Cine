from config.db import db, app, ma 

class usuarios(db.Model):
    __tablename__ = "tblusuarios"

    id = db.Column(db.Integer, primary_key=True)
    Rol = db.Column(db.String(50))
    nombre = db.Column(db.String(100))
    correo_electronico = db.Column(db.String(100))
    contrasena = db.Column(db.String(100))
    token = db.Column(db.String(500))

    def __init__(self, Rol, nombre, correo_electronico, contrasena):
        self.Rol = Rol
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        
with app.app_context():
    db.create_all()

class usuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','Rol','nombre','correo_electronico','contrasena')
#ESTE ES UN CAMPO VACIO
