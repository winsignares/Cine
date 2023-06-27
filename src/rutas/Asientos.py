from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_asientos = Blueprint("routes_asientos", __name__)
from Model.Funciones import funciones
from Model.Asientos import asientos
from Model.Compras import compras
from Model.peliculas import peliculas
from Model.Salas import salas
from Model.Usuarios import usuarios



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
    return jsonify({'id': new_compra.id})

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
    
@routes_asientos.route('/obtener_id_usuario', methods=['GET'])
def obtener_id_usuario():
    token = request.args.get('token')  # Obtener el token de la solicitud GET

    # Realizar una consulta a la base de datos para encontrar el registro con el token proporcionado
    usuario = usuarios.query.filter_by(token=token).first()

    if usuario:
        id_usuario = usuario.id  # Obtener el nombre del usuario

        return jsonify({'id_usuario': id_usuario})
    else:
        return jsonify({'error': 'Token de usuario inválido'})
    
@routes_asientos.route('/guardar_tickets', methods=['POST'])
def guardar_tickets():
    datos_ticket = request.get_json()

    # Obtener los datos del ticket desde el cuerpo de la solicitud
    id_usuarios = datos_ticket['id_usuarios']
    id_funcion = datos_ticket['id_funcion']
    cantidad_tickets = datos_ticket['cantidad_tickets']
    total_pagado = datos_ticket['total_pagado']
    fecha_compra = datos_ticket['fecha_compra']

    # Crear un nuevo registro de ticket en la tabla tblcompras
    nuevo_ticket = compras(
        id_usuarios=id_usuarios,
        id_funcion=id_funcion,
        cantidad_tickets=cantidad_tickets,
        total_pagado=total_pagado,
        fecha_compra=fecha_compra
    )

    db.session.add(nuevo_ticket)
    db.session.commit()

    # Obtener el ID del ticket recién creado
    id_ticket = nuevo_ticket.id

    # Resto del código...

    # Retornar la respuesta con el ID del ticket
    return jsonify({'id_ticket': id_ticket})
