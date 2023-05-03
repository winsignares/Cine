from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.Compras import Compra, CompraSchema

routes_compras = Blueprint("routes_rol", __name__)
#Roles
Compra_Schema = CompraSchema()
Compra_Schema = CompraSchema(many=True)

@routes_compras.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Dainer"

#Roles
#---------SAVE/CREAR------------
@routes_compras.route('/savesalas', methods=['POST'] )
def guardar_salas():
    #request.form['title']
    roles = request.json['roles']
    print(roles)
    new_rol = Compra(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/salas')


@routes_compras.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = CompraSchema.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(CompraSchema.dump(rol)) 

@routes_compras.route('/actualizar', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = Compra.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/Funciones')