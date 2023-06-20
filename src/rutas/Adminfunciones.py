from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.peliculas import peliculas, peliculasSchema
routes_AdminF = Blueprint("routes_AdminF", __name__)


@routes_AdminF.route('/indexAdminF', methods=['GET'] )
def indexAdminF():
    
    return render_template('/PeliculasWeb-main/Adminfunciones.html')