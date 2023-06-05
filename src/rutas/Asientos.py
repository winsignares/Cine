from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_asientos = Blueprint("routes_asientos", __name__)
from Model.Funciones import funciones


@routes_asientos.route('/indexAsientos', methods=['GET'] )
def indexAsientos():
    
    return render_template('/Main/IndexAsientos.html')

@routes_asientos.route('/mostrarticket', methods=['GET'])
def mostrar_ticket():
    titulo_pelicula = request.args.get('movie')
    resultado = db.session.query(tblfunciones, tblpeliculas, tblsalas).select_from(tblpeliculas).join(tblfunciones).join(tblsalas).all()
    i = 0
    tickets = []

    for tblfunciones, tblpeliculas, tblsalas in resultado:
        i += 1
        ticket = {
            'id': i,
            'titulo': tblpeliculas.titulo,
            'genero': tblpeliculas.genero,
            'duracion': tblpeliculas.duracion,
            'sinopsis': tblpeliculas.sinopsis,
            'director': tblpeliculas.director,
            'sala': tblsalas.nombre_sala,
            'fecha': tblfunciones.fecha,
            'precio': tblfunciones.precio
        }
        
        if tblpeliculas.titulo.lower() == titulo_pelicula.lower():
            tickets.append(ticket)

    return jsonify(tickets)
