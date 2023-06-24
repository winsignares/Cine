from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_asientos = Blueprint("routes_asientos", __name__)
from Model.Funciones import funciones
from Model.Asientos import asientos
from Model.Compras import compras
from Model.peliculas import peliculas
from Model.Salas import salas



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

#guardar asiento 
@routes_asientos.route('/save_asiento', methods=['POST'] )
def save_asientos():
    #request.form['title']
    id_sala = request.json['id_sala']
    id_funcion = request.json['id_funcion']
    numero = request.json['numero']
    estado = request.json['estado']
    print(numero,estado)
    new_asiento = asientos( id_sala, id_funcion, numero, estado)
    db.session.add(new_asiento)
    db.session.commit()
    return redirect('/Tasientos')
    
    
#mostrar asientos
@routes_asientos.route('/mostrar_asientos/', methods=['GET'])
def obtener_asientos():
    id_sala = request.args.get('id_sala')
    id_funcion = request.args.get('id_funcion')

    asientos_query = asientos.query.join(funciones, asientos.id_sala == funciones.id_sala).filter(funciones.id == id_funcion, asientos.id_sala == id_sala, asientos.id_funcion == id_funcion).all()

    resultado = []
    for asiento in asientos_query:
        resultado.append({
            'id': asiento.id,
            'numero': asiento.numero,
            'estado': asiento.estado
        })

    return jsonify(resultado)

