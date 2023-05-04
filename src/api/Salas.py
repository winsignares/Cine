
from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Salas import SalasSchema, SalasSchema

routes_salas = Blueprint("routes_rol", __name__)
#Roles
Sala_Schema = SalasSchema()
Salas_Schema = SalasSchema(many=True)

@routes_salas.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Dainer"


#Roles
#---------SAVE/CREAR------------
@routes_salas.route('/savesalas', methods=['POST'] )
def guardar_salas():
    #request.form['title']
    roles = request.json['roles']
    print(roles)
    new_rol = SalasSchema(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/salas')


@routes_salas.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = SalasSchema.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(SalasSchema.dump(rol)) 

@routes_salas.route('/actualizar', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = SalasSchema.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/salas')
