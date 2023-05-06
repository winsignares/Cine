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