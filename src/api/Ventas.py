
from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Ventas import VentasSchema, VentasSchema

routes_ventas = Blueprint("routes_ventas", __name__)
#Roles
Ventas_Schema = VentasSchema()
Ventas_Schema = VentasSchema(many=True)

@routes_ventas.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Dainer"


#Roles
#---------SAVE/CREAR------------
@routes_ventas.route('/savesalas', methods=['POST'] )
def guardar_salas():
    #request.form['title']
    roles = request.json['roles']
    print(roles)
    new_rol = VentasSchema(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/salas')


@routes_ventas.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = VentasSchema.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(VentasSchema.dump(rol)) 

@routes_ventas.route('/actualizar', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = VentasSchema.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/salas')