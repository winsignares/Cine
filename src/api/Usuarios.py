
from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Usuarios import Usuarios, RolesSchema

routes_roles = Blueprint("routes_Usuarios", __name__)
#Roles
Usuarios_schema = RolesSchema()
Usuarios_schema = RolesSchema(many=True)

@routes_roles.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Dainer!!"

#Roles
#---------SAVE/CREAR------------
@routes_roles.route('/saveroles', methods=['POST'] )
def guardar_roles():
    #request.form['title']
    #id_usuarios = request.form['id_usuarios']
    #id_roles_usuarios = request.form['id_roles_usuarios']
    #Nombre = request.form['Nombre']git 
    #Correo_electronico = request.form['Correo_electronico']
    #Contraseña = request.form['Contraseña']
    roles = request.json['roles']
    print(roles)
    new_rol = Usuarios_schema(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/Usuarios')


@routes_roles.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id_usuarios = request.form['id_usuarios']
    #id_roles_usuarios = request.form['id_roles_usuarios']
    #Nombre = request.form['Nombre']git 
    #Correo_electronico = request.form['Correo_electronico']
    #Contraseña = request.form['Contraseña']
    rol = Usuarios_schema.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(Usuarios_schema.dump(rol)) 

@routes_roles.route('/actualizar', methods=['POST'] )
def actualizar():
    #id_usuarios = request.form['id_usuarios']
    #id_roles_usuarios = request.form['id_roles_usuarios']
    #Nombre = request.form['Nombre']git 
    #Correo_electronico = request.form['Correo_electronico']
    #Contraseña = request.form['Contraseña']
    id = request.json['id']
    rol = request.json['roles']
    Usuarios_schema = Usuarios_schema.query.get(id)
    Usuarios_schema.roles = rol
    db.session.commit()
    return redirect('/Usuarios')
