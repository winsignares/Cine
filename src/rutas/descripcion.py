from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.peliculas import peliculas, peliculasSchema
routes_Descripcion = Blueprint("routes_Descripcion", __name__)


@routes_Descripcion.route('/indexDescripcion', methods=['GET'] )
def indexDescripcion():
    
    return render_template('/Main/DESCRIPCIONES/Descripcion.html')

@app.route('/mostrar', methods=['GET'])
def mostar():
    datos= {}
    resultado = db.session.query(peliculas).select_from(peliculas).all()
    i=0
    users = []
    for peliculas in resultado:
        i+=1	       
        datos[i] = {
            'titulo':peliculas.titulo,
            'genero':peliculas.genero,
            'duracion':peliculas.duracion,
            'sinopsis':peliculas.sinopsis,
            'director':peliculas.director,
            'imagen':peliculas.imagen
        }  
        users.append(datos)
        print("\n",users,"\n")
    return jsonify(datos)