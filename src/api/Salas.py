from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Salas import salas, salasSchema

routes_salas = Blueprint("routes_salas", __name__)
#Roles
sala_schema = salasSchema()
salas_schema = salasSchema(many=True)

@routes_salas.route('/indexsalas', methods=['GET'] )
def indexsalas():
    return "hello world"

#-----------TOKEN-------------
routes_salas.route('/Tsala', methods=['GET'])
def Sala():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = salas.query.all()
        result_sala = salasSchema.dump(returnall)
        return jsonify(result_sala)
    else:
        return vf
    
#---------SAVE/CREAR------------
@routes_salas.route('/save_sala', methods=['POST'])
def save_sala():
    nombre_sala = request.json['nombre_sala']
    capacidad = request.json['capacidad']
    new_room = salas(nombre_sala,capacidad)
    db.session.add(new_room)
    db.session.commit()
    return redirect ("/Tsala")

#------------DELETE/ELIMINAR------------
@routes_salas.route('/delete_salas/<id>', methods=['GET'])
def delete_salas(id):
    print(id)
    room = salas.query.get(id)
    mensaje = {}
    if(room):    
        db.session.delete(room)
        db.session.commit()
        mensaje = "Dato eliminado"
    else:
        mensaje = "dato no encontrado"
    response = {
        'status': 200,
        'body': mensaje
    }
    return jsonify(response)

#------------UPDATE/ACTUALIZAR-----------
@routes_salas.route('/update_sala', methods=['POST'])
def update_sala():
    id = request.json['id']
    nombre_sala = request.json['nombre_sala']
    capacidad = request.json['capacidad']
    room = salas.query.get(id)
    room.nombre_sala = nombre_sala
    room.capacidad = capacidad
    db.session.commit()
    return redirect ('/Tsala') 