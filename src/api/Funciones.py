from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Funciones import funciones, funcionesSchema

routes_funciones = Blueprint("routes_funcion", __name__)

funcion_schema = funcionesSchema
funciones_schema = funcionesSchema(many=True)

@routes_funciones.route('/indexfuncion', methods=['GET'])
def funciones():
    return('hello world')
#TOKEN
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
    
@routes_funciones.route('/savefuncion', methods=['POST'])
def savefuncion():
    id_pelicula = request.json['id_pelicula']
    id_sala = request.json['id_sala']
    fecha = request.json['fecha']
    precio = request.json['precio']
    print(id_pelicula,id_sala,fecha,precio)
    db.session.add(id_pelicula,id_sala,fecha,precio)
    db.session.commit()
    return('/Tfuncion')
