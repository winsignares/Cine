from config.db import db, app, ma 

class usuarios(db.Model):
    __tablename__ = "tblusuarios"

    id = db.Column(db.Integer, primary_key=True)
    Rol = db.Column(db.String(20))
    nombre = db.Column(db.String(50))
    correo_electronico = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))

<<<<<<< HEAD
    def __init__(self, Rol, nombre, correo_electronico, contraseña):
        self.Rol = Rol
=======
    def __init__(self, id_roles_usuarios, nombre, correo_electronico, contrasena):
        self.id_roles_usuarios = id_roles_usuarios
>>>>>>> 6cc481dac2b57a41ba0fc38cab2e5d0189e8896d
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        
with app.app_context():
    db.create_all()

class usuariosSchema(ma.Schema):
    class Meta:
<<<<<<< HEAD
        fields = ('id','Rol','nombre','correo_electronico','contraseña')
=======
        fields = ('id','id_roles_usuarios','nombre','correo_electronico','contrasena')
>>>>>>> 6cc481dac2b57a41ba0fc38cab2e5d0189e8896d
