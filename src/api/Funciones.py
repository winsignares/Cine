from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Funciones import Funciones, Funciones

routes_funciones = Blueprint("routes_rol", __name__)
#Roles
Funciones = Funciones()
Funciones = Funciones(many=True)

@routes_funciones.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Dainer"

#Roles
#---------SAVE/CREAR------------
@routes_funciones.route('/savesalas', methods=['POST'] )
def guardar_salas():
    #request.form['title']
    roles = request.json['roles']
    print(roles)
    new_rol = Funciones(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/salas')


@routes_funciones.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = Funciones.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(Funciones.dump(rol)) 

@routes_funciones.route('/actualizar', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = Funciones.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/Funciones')