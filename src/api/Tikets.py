
from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.tikets import Tikets, Tikets

routes_tikets = Blueprint("routes_rol", __name__)
#Roles
TiketsSchema = Tikets()
TiketSchema = Tikets(many=True)

@routes_tikets.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Dainer"


#Roles
#---------SAVE/CREAR------------
@routes_tikets.route('/savesalas', methods=['POST'] )
def guardar_salas():
    #request.form['title']
    roles = request.json['roles']
    print(roles)
    new_rol = TiketsSchema(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/salas')


@routes_tikets.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = TiketsSchema.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(TiketsSchema.dump(rol)) 

@routes_tikets.route('/actualizar', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = TiketsSchema.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/tikets')