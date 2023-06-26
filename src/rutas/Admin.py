from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.peliculas import peliculas, peliculasSchema
from Model.Funciones import funciones, funcionesSchema
routes_Admin = Blueprint("routes_Admin", __name__)


@routes_Admin.route('/indexAdmin', methods=['GET'] )
def indexAdmin():
    
    return render_template('/PeliculasWeb-main/Admin.html')
#guardar
@routes_Admin.route('/saveAdmin', methods=['POST'] )
def saveAdmin():
    
    titulo = request.json['titulo']
    genero = request.json['genero']
    duracion = request.json['duracion']
    sinopsis = request.json['sinopsis']
    director = request.json['director']
    imagen = request.json['imagen']
    video = request.json['video']
    
    # Crear una nueva instancia de usuarios con los datos proporcionados y el token generado
    new_pelis = peliculas(titulo, genero, duracion, sinopsis, director, imagen, video)
    
    # Agregar el nuevo usuario a la sesión y guardar los cambios en la base de datos
    db.session.add(new_pelis)
    db.session.commit()
    # return '/showAdmin'

@routes_Admin.route('/mostrar_pelicula', methods=['GET'])
def Peli():
    returnall = peliculas.query.all()
    peliculas_schema = peliculasSchema(many=True)
    result_peli = peliculas_schema.dump(returnall)
    return jsonify(result_peli)


@routes_Admin.route('/saveFuncion', methods=['POST'] )
def saveFuncion():
    
    id_peliculas = request.json['id_peliculas']
    id_sala = request.json['id_sala']
    fecha = request.json['fecha']
    precio = request.json['precio']

    
    # Crear una nueva instancia de usuarios con los datos proporcionados y el token generado
    new_funcion = funciones(id_peliculas, id_sala, fecha, precio)
    
    # Agregar el nuevo usuario a la sesión y guardar los cambios en la base de datos
    db.session.add(new_funcion)
    db.session.commit()
    # return '/showAdmin'

@routes_Admin.route('/mostrar_funciones', methods=['GET'])
def Funci():
    returnall = funciones.query.all()
    funciones_schema = funcionesSchema(many=True)
    result_func = funciones_schema.dump(returnall)
    return jsonify(result_func)
