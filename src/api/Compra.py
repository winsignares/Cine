from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Compras import compras , comprasSchema

routes_compra = Blueprint("routes_compras", __name__)

compra_schema = comprasSchema 
compras_schema = comprasSchema (many=True)

@routes_compra.route('/indexcompras', methods=['GET'] )
def compras():
    return ('hello world')

#token
@routes_compra.route('/Tcompra', methods=['GET'])
def shop():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = compras.query.all()
        result_compra = comprasSchema.dump(returnall)
        return jsonify(result_compra)
    else:
        return vf
    
#---------SAVE/CREAR------------
@routes_compra.route('/savecompras', methods=['POST'])
def savecompras():
    id_usuarios = request.json['id_usuarios']
    id_funcion = request.json['id_funcion']
    cantidad_tickets = request.json['cantidad_tickets']
    total_pagado = request.json['total_pagado']
    fecha_compra = request.json['fecha_compra']
    print(id_usuarios,id_funcion,cantidad_tickets,total_pagado,fecha_compra)
    new_compra = compras(id_usuarios,id_funcion,cantidad_tickets,total_pagado,fecha_compra)
    db.session.add(new_compra)
    db.session.commit()
    return('/Tcompra')
