from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.tickets import tickets, ticketsSchema

routes_tickets = Blueprint("routes_ticket", __name__)
#Roles
ticket_schema = ticketsSchema()
tickets_schema = ticketsSchema(many=True)

@routes_tickets.route('/indexticket', methods=['GET'] )
def indexticket():
    return "hello world"

#TOKEN
routes_tickets.route('/Tticket', methods=['GET'])
def Ticket():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = tickets.query.all()
        result_ticket = tickets_schema.dump(returnall)
        return jsonify(result_ticket)
    else:
        return vf

@routes_tickets.route('/save_ticket', methods=['POST'])
def save_ticket():
    id_compra = request.json['nombre_sala']
    id_funcion = request.json['capacidad']
    asiento = request.json['asiento']
    fecha_emision = request.json['fecha_emision']
    new_ticket = tickets(id_compra, id_funcion, asiento, fecha_emision)
    db.session.add(new_ticket)
    db.session.commit()
    return redirect ("/Tticket")