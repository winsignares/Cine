from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Funciones import funciones, funcionesSchema

routes_funciones = Blueprint("routes_funcion", __name__)

funcion_schema = funcionesSchema
funciones_schema = funcionesSchema(many=True)

@routes_funciones.route('/indexfuncion', methods=['GET'])
def funcione():
    return('hello world')

#-----------TOKEN-------------
@routes_funciones.route('/Tfuncion', methods=['GET'])
def funcion():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = funciones.query.all()
        result_compra = funcionesSchema.dump(returnall)
        return jsonify(result_compra)
    else:
        return vf
#---------SAVE/CREAR------------
@routes_funciones.route('/save_funcion', methods=['POST'])
def save_funcion():
    id_peliculas = request.json['id_peliculas']
    id_sala = request.json['id_sala']
    fecha = request.json['fecha']
    precio = request.json['precio']
    print(id_peliculas,id_sala,fecha,precio)
    new_funcion = funciones(id_peliculas, id_sala, fecha, precio)
    db.session.add(new_funcion)
    db.session.commit()
    return('/Tfuncion')

#------------DELETE/ELIMINAR------------
@routes_funciones.route('/delete_funcion/<id>', methods=['GET'] )
def delete_Funcion(id):
    print(id)
    Funtion = funciones.query.get(id)
    mensaje = {}
    if(Funtion):    
        db.session.delete(Funtion)
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
@routes_funciones.route('/update_funcion', methods=['POST'])
def update_funcion():
    id = request.json['id']
    id_peliculas = request.json['id_peliculas']
    id_sala = request.json['id_sala']
    fecha = request.json['fecha']
    precio = request.json['precio']
    fun = funciones.query.get(id)
    fun.id_peliculas = id_peliculas
    fun.id_sala = id_sala
    fun.fecha = fecha
    fun.precio = precio
    db.session.commit()
    return redirect('/Tfuncion')