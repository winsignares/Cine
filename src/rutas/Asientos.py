from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_asientos = Blueprint("routes_asientos", __name__)
from Model.Funciones import funciones


@routes_asientos.route('/indexAsientos', methods=['GET'] )
def indexAsientos():
    
    return render_template('/Main/IndexAsientos.html')

@routes_asientos.route('/mostrarticket', methods=['GET'])
def mostar():
    datos= {}
    resultado = db.session.query( tblfunciones ,tblpeliculas, tblsalas).select_from(tblfunciones).join(tblpeliculas).join(tblsalas).all()
    i=0
    users = []
    for tblfunciones, tblpeliculas, tblsalas  in resultado:
        i+=1	       
        datos[i] = {
            'nombre': tblpeliculas.nombre,
            'sala': tblsalas.nombre_sala,
            'funcion': tblfunciones.id,
    
        }  
        users.append(datos)
    return jsonify(datos)  
