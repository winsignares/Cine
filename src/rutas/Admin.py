from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.peliculas import peliculas
routes_Admin = Blueprint("routes_Admin", __name__)


@routes_Admin.route('/indexAdmin', methods=['GET'] )
def indexAdmin():
    return render_template('/Main/IndexAdmin.html')
@routes_Admin.route('/addPelis', methods=['POST'] )
def addPelis():
    titulo = request.json['titulo']
    genero = request.json['genero']
    duracion = request.json['duracion']
    sinopsis = request.json['sinopsis']
    director = request.json['director']
    imagen = request.json['imagen']
    video = request.json['video']
    new_pelis = peliculas(titulo,genero,duracion,sinopsis,director,imagen,video)
    db.session.add(new_pelis)
    db.session.commit()
    print("ok")
    return "/fronted/indexmainlogin"
