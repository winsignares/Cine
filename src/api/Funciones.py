from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Funciones import Funciones, FuncionesSchema

routes_funciones = Blueprint("routes_funciones", __name__)
#Roles
Funcion_Schema = FuncionesSchema()
Funciones_Schema = FuncionesSchema(many=True)

@routes_funciones.route('/', methods=['GET'] )
def indexRoles():
    
    return "index"

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
    rol = FuncionesSchema.query.get(id)
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