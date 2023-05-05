from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Usuarios import usuarios,usuariosSchema

routes_usuarios = Blueprint("routes_usuarios", __name__)

#Roles
usuario_schema = usuariosSchema()
usuarios_schema = usuariosSchema(many=True)


@routes_usuarios.route('/indexusuarios', methods=['GET'] )
def indexusuarios():
    return "hello world"

@routes_usuarios.route('/Usuarios', methods=['GET'])
def Usuari():    
    returnall = usuarios.query.all()
   
    resultado_usuarios = usuariosSchema.dump(returnall)
    return jsonify(resultado_usuarios)


@routes_usuarios.route('/save_user', methods=['POST'] )
def guardar_Users():
    id_roles_usuarios = request.json['id_roles_usuarios']
    nombre = request.json['nombre']
    correo_electronico = request.json['correo_electronico']
    contraseña = request.json['contraseña']
    print(id_roles_usuarios,nombre,correo_electronico,contraseña)
    new_Users = usuarios(id_roles_usuarios,nombre,correo_electronico,contraseña)
    db.session.add(new_Users)
    db.session.commit()
    return redirect('/Usuarios')


@routes_usuarios.route('/delete_user/<id>', methods=['GET'] )
def delete_User(id):
    print(id)
    user = usuarios.query.get(id)
    mensaje = {}
    if(user):    
        db.session.delete(user)
        db.session.commit()
        mensaje = "Dato eliminado"
    else:
        mensaje = "dato no encontrado"
    response = {
        'status': 200,
        'body': mensaje
    }
    return jsonify(response)

@routes_usuarios.route('/update_user', methods=['POST'])
def update_user():
    id = request.json['id']
    id_roles_usuarios = request.json['id_roles_usuarios']
    nombre = request.json['nombre']
    correo_electronico= request.json['correo_electronico']
    contraseña= request.json['contraseña']
    users = usuarios.query.get(id)
    users.id_roles_usuarios = id_roles_usuarios
    users.nombre= nombre
    users.correo_electronico = correo_electronico
    users.contraseña= contraseña
    db.session.commit()
    return redirect('/Usuarios')
    