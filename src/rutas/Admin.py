from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.peliculas import peliculas, peliculasSchema
routes_Admin = Blueprint("routes_Admin", __name__)


@routes_Admin.route('/indexAdmin', methods=['GET'] )
def indexAdmin():
    
    return render_template('/PeliculasWeb-main/Admin.html')
@routes_Admin.route('/saveAdmin', methods=['GET'] )
def saveAdmin():
    
    id = request.json['id']
    titulo = request.json['titulo']
    genero = request.json['genero']
    duracion = request.json['duracion']
    sinopsis = request.json['sinopsis']
    director = request.json['director']
    imagen = request.json['imagen']
    
    # Crear una nueva instancia de usuarios con los datos proporcionados y el token generado
    new_pelis = peliculas(id,titulo, genero, duracion, sinopsis, director, imagen)
    
    # Agregar el nuevo usuario a la sesión y guardar los cambios en la base de datos
    db.session.add(new_pelis)
    db.session.commit()
    # return '/showAdmin'

# @routes_Admin.route('/showAdmin', methods=['GET'] )
# def showAdmin():
    # Retornar los datos ingresados a la BD
    #descpeli = db.Model.metadata.tables['tblpeliculas'] 
    peliculasDB = db.session.query(peliculas).all()
    i = 0
    for peli in peliculasDB:
        i += 1
        datos = {
            'id': peli.id,
            'titulo': peli.titulo,
            'genero': peli.genero,
            'duracion': peli.duracion,
            'sinopsis': peli.sinopsis,
            'director': peli.director,
            'imagen': peli.imagen,
            'video': peli.video
        }
    return jsonify(datos)