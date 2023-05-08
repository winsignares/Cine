from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Peliculas import peliculas, peliculasSchema

routes_peliculas = Blueprint("routes_pelicula", __name__)

pelicula_schema = peliculasSchema
peliculas_schema = peliculasSchema(many=True)

@routes_peliculas.route('/indexpeliculas', methods=['GET'] )
def indexRoles():
    return "hello world"

#TOKEN
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
    
