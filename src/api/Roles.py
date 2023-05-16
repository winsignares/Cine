from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.RolesUsuario import rolesUsuarios, rolesSchema

routes_roles = Blueprint("routes_rol", __name__)
#Roles
rolesusuario_schema = rolesSchema()
rolesusuarios_schema = rolesSchema(many=True)

@routes_roles.route('/indexroles', methods=['GET'] )
def indexRoles():
    return "hello world"

#-----------TOKEN-------------
@routes_roles.route('/Troles', methods=['GET'])
def Rol():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = rolesUsuarios.query.all()
        result_rusuarios = rolesusuarios_schema.dump(returnall)
        return jsonify(result_rusuarios)
    else:
        return vf
#Roles
#---------SAVE/CREAR------------
@routes_roles.route('/save_roles', methods=['POST'] )
def guardar_roles():
    #request.form['title']
    roles = request.json['roles']
    print(roles)
    new_rol = rolesUsuarios(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/Trusuarios')

#------------DELETE/ELIMINAR------------
@routes_roles.route('/eliminar_roles/<id>', methods=['GET'] )
def eliminar_roles(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = rolesUsuarios.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(rolesusuario_schema.dump(rol)) 

#------------UPDATE/ACTUALIZAR-----------
@routes_roles.route('/actualizar_roles', methods=['POST'] )
def actualizar_roles():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = rolesUsuarios.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/Trusuarios')