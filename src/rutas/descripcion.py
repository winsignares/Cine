from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.peliculas import peliculas, peliculasSchema
routes_Descripcion = Blueprint("routes_Descripcion", __name__)


@routes_Descripcion.route('/indexDescripcion', methods=['GET'] )
def indexDescripcion():
    
    return render_template('/Main/IndexDescripcion.html')

@routes_Descripcion.route('/mostrarpelidesc', methods=['GET'])
def mostrar_pelicula():
    titulo = request.args.get('titulo')
    datos = {}
    descpeli = db.Model.metadata.tables['tblpeliculas'] 
    peliculas = db.session.query(descpeli).filter_by(titulo=titulo).first()
    i = 0
    for descpeli in peliculas:
        i += 1
        datos = {
            'titulo': peliculas.titulo,
            'genero': peliculas.genero,
            'duracion': peliculas.duracion,
            'sinopsis': peliculas.sinopsis,
            'director': peliculas.director,
            'imagen': peliculas.imagen,
            'video': peliculas.video
        }
        return jsonify(datos)
    else:
        return jsonify({'error': 'Película no encontrada'})

@routes_Descripcion.route('/mostrartrailer', methods=['GET'])
def mostrar_triler():
    titulo = request.args.get('titulo')
    datos = {}
    descpeli = db.Model.metadata.tables['tblpeliculas'] 
    peliculas = db.session.query(descpeli).filter_by(titulo=titulo).first()
    i = 0
    for descpeli in peliculas:
        i += 1
        datos = {
            'titulo': peliculas.titulo,
            'video': peliculas.video
        }
        return jsonify(datos)
    else:
        return jsonify({'error': 'Película no encontrada'})

