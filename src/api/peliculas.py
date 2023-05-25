from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.peliculas import Peliculas, peliculaSchema

routes_peliculas = Blueprint("routes_pelis", __name__)
#Roles
pelicula_Schema = peliculaSchema()
peliculas_Schema = peliculaSchema(many=True)

@routes_peliculas.route('/indexDescripcion', methods=['GET'] )
def indexDescripcion():    
    return "Hola Mundo!!"

#Atributos pelis
'''
id, titulo, genero, duracion, sinopsis, director, img
'''
#---------SAVE/CREAR------------
@routes_peliculas.route('/savepelis', methods=['POST'] )
def guardar_roles():
    #request.form['title'] atributos de la tabla
    titulo = request.json['titulo']
    genero = request.json['genero']
    duracion = request.json['duracion']
    sinopsis = request.json['sinopsis']
    director = request.json['director']
    img = request.json['img']
    print(titulo)
    new_title = peliculas_Schema(titulo,genero,duracion,sinopsis,director,img)
    db.session.add(new_title)
    db.session.commit()
    return redirect('/indexDescripcion')


@routes_peliculas.route('/deletePelis', methods=['GET'] )
def eliminar(id):
    #id = request.args.get('id')
    #id = request.json['id']
    titulo = pelicula_Schema.query.get(id)
    db.session.delete(titulo)
    db.session.commit()
    return jsonify(peliculaSchema.dump(titulo)) 

@routes_peliculas.route('/Update_pelis', methods=['POST'] )
def actualizar():
    #id = request.form['id']
    #Nombre = request.form['Nombre']
    #Precio = request.form['Precio']git 
    id = request.json['id']
    rol = request.json['roles']
    rusuario = pelicula_Schema.query.get(id)
    rusuario.roles = rol
    db.session.commit()
    return redirect('/rusuarios')

