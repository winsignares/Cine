from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_asientos = Blueprint("routes_asientos", __name__)
from Model.Funciones import funciones
from Model.Compras import compras


@routes_asientos.route('/indexAsientos', methods=['GET'] )
def indexAsientos():
    
    return render_template('/Main/IndexAsientos.html')



@routes_asientos.route('/buscarfunciones', methods=['GET'])
def buscar_funciones():
    titulo = request.args.get('titulo')
    funciones = db.Model.metadata.tables['tblfunciones']
    peliculas = db.Model.metadata.tables['tblpeliculas']
    resultado = db.session.query(funciones).join(peliculas).filter_by(titulo=titulo).all()

    funciones = []
    for funcion in resultado:
        funcion_data = {
            'id': funcion.id,
            'id_peliculas': funcion.id_peliculas,
            'id_sala': funcion.id_sala,
            'fecha': funcion.fecha,
            'precio': funcion.precio
        }
        funciones.append(funcion_data)

    return jsonify(funciones)

#guardar
@routes_asientos.route('/save_compras', methods=['POST'])
def savecompras():
    id_usuarios = request.json['id_usuarios']
    id_funcion = request.json['id_funcion']
    cantidad_tickets = request.json['cantidad_tickets']
    total_pagado = request.json['total_pagado']
    fecha_compra = request.json['fecha_compra']
    print(id_usuarios, id_funcion, cantidad_tickets, total_pagado, fecha_compra)
    new_compra = compras(id_usuarios, id_funcion, cantidad_tickets, total_pagado, fecha_compra)
    db.session.add(new_compra)
    db.session.commit()
    return '/Tcompra'
#mostrar asientos


