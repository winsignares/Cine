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

#TOKEN
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