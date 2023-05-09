from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Ventas import ventas, ventasSchema

routes_ventas = Blueprint("routes_ventas", __name__)
#Roles
venta_schema = ventasSchema()
ventas_schema = ventasSchema(many=True)

@routes_ventas.route('/indexventa', methods=['GET'] )
def indexventa():
    return "hello world"

#-----------TOKEN-------------
@routes_ventas.route('/Tventa', methods=['GET'])
def Venta():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = ventas.query.all()
        result_venta = ventasSchema.dump(returnall)
        return jsonify(result_venta)
    else:
        return vf
    
#---------SAVE/CREAR------------
@routes_ventas.route('save_venta', methods=['POST'])
def save_venta():
    id_funcion = request.json['id_funcion']
    fecha = request.json['fecha']
    cantidad_tickets = request.json['cantidad_tickets']
    precio_total = request.json['precio_total']
    new_venta = ventas(id_funcion,fecha,cantidad_tickets,precio_total)
    db.session.add(new_venta)
    db.session.commit()
    return redirect('/Tventa')

#------------DELETE/ELIMINAR------------
@routes_ventas.route('/delete_venta/<id>', methods=['GET'] )
def delete_venta(id):
    print(id)
    sale = ventas.query.get(id)
    mensaje = {}
    if(sale):    
        db.session.delete(sale)
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
@routes_ventas.route('update_venta', methods=['POST'])
def update_venta():
    id = request.json['id']
    id_funcion = request.json['id_funcion']
    fecha = request.json['fecha']
    cantidad_tickets = request.json['cantidad_tickets']
    precio_total = request.json['precio_total']
    sales = ventas.query.get(id)
    sales.id = id_funcion
    sales.fecha = fecha
    sales.cantidad_tickets = cantidad_tickets
    sales.precio_total = cantidad_tickets
    sales.precio_total = precio_total
    db.session.commit()
    return redirect('/Tventa')