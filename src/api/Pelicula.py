from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.peliculas import peliculas, peliculasSchema

routes_peliculas = Blueprint("routes_pelicula", __name__)

pelicula_schema = peliculasSchema
peliculas_schema = peliculasSchema(many=True)

@routes_peliculas.route('/indexpeliculas', methods=['GET'] )
def indexRoles():
    return "hello world"

#-----------TOKEN-------------
@routes_peliculas.route('/Tpelicula', methods=['GET'])
def Peli():    
    token = request.headers['Authorization']
    token = token.replace("Bearer","")
    token = token.replace(" ","")
    vf = verificar_token(token)
    if vf['error'] == False:
        returnall = peliculas.query.all()
        result_peli = peliculasSchema.dump(returnall)
        return jsonify(result_peli)
    else:
        return vf
    
#---------SAVE/CREAR------------
@routes_peliculas.route('/save_pelicula', methods=['POST'])
def save_pelicula():
    titulo = request.json['titulo']
    genero = request.json['genero']
    duracion = request.json['duracion']
    sinopsis = request.json['sinopsis']
    director = request.json['director']
    imagen = request.json['imagen']
    print(titulo,genero,duracion,sinopsis,director,imagen)
    new_movie = peliculas(titulo,genero,duracion,sinopsis,director,imagen)
    db.session.add(new_movie)
    db.session.commit()
    return('/Tpelicula')

#------------DELETE/ELIMINAR------------
@routes_peliculas.route('/delete_pelicula/<id>', methods=['GET'])
def delete_pelicula(id):
    print(id)
    movie = peliculas.query.get(id)
    mensaje = {}
    if(movie):    
        db.session.delete(movie)
        db.session.commit()
        mensaje = "Dato eliminado"
    else:
        mensaje = "dato no encontrado"
    response = {
        'status': 200,
        'body': mensaje
    }
    return jsonify(response)

#------------UPDATE/ACTUALIZAR-----------
@routes_peliculas.route('/update_pelicula', methods=['POST'])
def update_pelicula():
    id = request.json['id']
    titulo = request.json['titulo']
    genero = request.json['genero']
    duracion = request.json['duracion']
    sinopsis = request.json['sinopsis']
    director = request.json['director']
    imagen = request.json['imagen']
    movie = peliculas.query.get(id)
    movie.titulo = titulo
    movie.genero = genero
    movie.duracion = duracion
    movie.sinopsis = sinopsis
    movie.director = director
    movie.imagen = imagen
    db.session.commit()
    return redirect ('/Tpelicula') 