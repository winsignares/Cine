from config.db import db, app, ma 

class usuarios(db.Model):
    __tablename__ = "tblusuarios"

    id = db.Column(db.Integer, primary_key=True)
    id_roles_usuarios = db.Column(db.Integer, db.ForeignKey('tblrolesusuarios.id'))
    nombre = db.Column(db.String(50))
    correo_electronico = db.Column(db.String(50))
    contraseña = db.Column(db.String(50))

    def __init__(self, id_roles_usuarios, nombre, correo_electronico, contraseña):
        self.id_roles_usuarios = id_roles_usuarios
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contraseña = contraseña
        
with app.app_context():
    db.create_all()

class usuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','id_roles_usuarios','Nombre','Correo_electronico','Contraseña')