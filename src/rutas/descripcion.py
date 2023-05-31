from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.peliculas import peliculas, peliculasSchema
routes_Descripcion = Blueprint("routes_Descripcion", __name__)


@routes_Descripcion.route('/indexDescripcion', methods=['GET'] )
def indexDescripcion():
    
    return render_template('/Main/IndexDescripcion.html')

@app.route('/mostrar', methods=['GET'])
def mostar():
    print("get data...\n")
    datos= {}
    resultado = db.session.query(peliculas).select_from(peliculas).all()
    i=0
    users = []
    for pelis in resultado:
        i+=1	       
        datos[i] = {
            'titulo':pelis.titulo,
            'genero':pelis.genero,
            'duracion':pelis.duracion,
            'sinopsis':pelis.sinopsis,
            'director':pelis.director,
            'imagen':pelis.imagen,
            'video':pelis.video,

        }  
    users.append(datos)
    print("\n",users,"\n")
    return jsonify(datos)