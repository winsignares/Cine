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
        result_ticket = ticketsSchema.dump(returnall)
        return jsonify(result_ticket)
    else:
        return vf