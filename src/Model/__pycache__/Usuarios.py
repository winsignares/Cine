from config.db import db, app, ma 

class RolesUsuarios(db.Model):
    __tablename__ = "Usuarios"

    id_usuarios = db.Column(db.Integer, primary_key=True)
    id_roles_usuarios = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50))
    Correo_electronico = db.Column(db.String(50))
    Contraseña = db.Column(db.String(50))

    def __init__(self, Usuaios):
        self.id_usuarios = Usuaios
        
with app.app_context():
    db.create_all()

class RolesSchema(ma.Schema):
    class Meta:
        fields = ('id_usuarios','id_roles_usuarios','Nombre','Correo_electronico','Contraseña')