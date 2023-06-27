from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_CTicket = Blueprint("routes_CTicket", __name__)
from Model.tickets import tickets
from Model.Compras import compras
from Model.Usuarios import usuarios


@routes_CTicket.route('/CTicket', methods=['GET'] )
def indexTicket():
    
    return render_template('/Main/IndexTicket.html')

@routes_CTicket.route('/mostrar_asientos/', methods=['GET'])
def obtener_tickets_propietario():
    id_compra = request.args.get('idCompra')

    # Obtener los tickets de la compra
    tickets_query = tickets.query.join(compras, tickets.id_compra == compras.id).filter(compras.id == id_compra).all()

    resultado = []
    for ticket in tickets_query:
        # Obtener el propietario del usuario
        propietario = usuarios.query.filter(usuarios.id == ticket.id_compra).first()

        resultado.append({
            'id_ticket': ticket.id,
            'propietario': propietario.nombre
        })

    return jsonify(resultado)

