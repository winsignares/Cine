
from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.tikets import Tickets, TicketsSchema

routes_tickets = Blueprint("routes_tickets", __name__)
#Roles
Ticket_Schema = TicketsSchema()
Tickets_Schema = TicketsSchema(many=True)

@routes_tickets.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Dainer"


#Roles
#---------SAVE/CREAR------------
@routes_tickets.route('/savesalas', methods=['POST'] )
def guardar_salas():
    #request.form['title']
    roles = request.json['roles']
    print(roles)
    new_rol = Tickets(roles)
    db.session.add(new_rol)
    db.session.commit()
    return redirect('/salas')


@routes_tickets.route('/eliminar/<id>', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    rol = TicketsSchema.query.get(id)
    db.session.delete(rol)
    db.session.commit()
    return jsonify(TicketsSchema.dump(rol)) 

@routes_tickets.route('/actualizar', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = TicketsSchema.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/tickets')