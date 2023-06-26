from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import usuarios
routes_CTicket = Blueprint("routes_CTicket", __name__)


@routes_CTicket.route('/CTicket', methods=['GET'] )
def indexTicket():
    
    return render_template('/Main/IndexTicket.html')

from sqlalchemy import text

@routes_CTicket.route('/crear_ticketes', methods=['GET'])
def obtener_tickets():
    id_usuario = request.args.get('id_usuario')
    id_compra = request.args.get('id_compra')

    # Aquí debes implementar la lógica para obtener los tickets de la base de datos
    # Utiliza la consulta SQL mencionada anteriormente para obtener los datos necesarios

    query = text("""
        SELECT t.id, t.id_compra, t.id_funcion, t.id_asiento, t.fecha_emision
        FROM tbltickets t
        INNER JOIN tblcompras c ON t.id_compra = c.id
        WHERE c.id = :id_compra AND c.id_usuarios = :id_usuario
    """)
    
    tickets_query = db.session.execute(query, {"id_compra": id_compra, "id_usuario": id_usuario})
    tickets = tickets_query.fetchall()

    resultado = []
    for ticket in tickets:
        resultado.append({
            'id': ticket.id,
            'id_compra': ticket.id_compra,
            'id_funcion': ticket.id_funcion,
            'id_asiento': ticket.id_asiento,
            'fecha_emision': ticket.fecha_emision
        })

    return jsonify(resultado)


@routes_CTicket.route('/obtener_id_usuario', methods=['GET'])
def obtener_id_usuario():
    token = request.args.get('token')  # Obtener el token de la solicitud GET

    # Realizar una consulta a la base de datos para encontrar el registro con el token proporcionado
    usuario = usuarios.query.filter_by(token=token).first()

    if usuario:
        id_usuario = usuario.id  # Obtener el ID del usuario

        return jsonify({'id_usuario': id_usuario})
    else:
        return jsonify({'error': 'Token de usuario inválido'})
