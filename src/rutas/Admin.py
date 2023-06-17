from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.peliculas import peliculas, peliculasSchema
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
