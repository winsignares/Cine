from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Asientos import asientos , asientosSchema

routes_Iasiento = Blueprint("routes_asiento", __name__)

asiento_schema = asientosSchema 
asientos_schema = asientosSchema (many=True)

@routes_Iasiento.route('/indexasientos', methods=['GET'] )
def asientos():
    return ('hello world')

#-----------TOKEN-------------
@routes_Iasiento.route('/Tasiento', methods=['GET'])
def chair():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = asientos.query.all()
        result_compra = asientosSchema.dump(returnall)
        return jsonify(result_compra)
    else:
        return vf

#---------SAVE/CREAR------------
@routes_Iasiento.route('/save_asiento', methods=['POST'] )
def guardar_roles():
    #request.form['title']
    numero = request.json['numero']
    estado = request.json['estado']
    print(numero,estado)
    new_asiento = asientos(numero, estado)
    db.session.add(new_asiento)
    db.session.commit()
    return redirect('/Tasientos')

#------------DELETE/ELIMINAR------------
@routes_Iasiento.route('/delete_asientos/<id>', methods=['GET'] )
def eliminar_asientos(id):
    print(id)
    Asientos = asientos.query.get(id)
    mensaje = {}
    if(Asientos):    
        db.session.delete(Asientos)
        db.session.commit()
        mensaje = "Dato eliminado"
    else:
        mensaje = "dato no encontrado"
    response = {
        'status': 200,
        'body': mensaje
    }
    return jsonify(response)
