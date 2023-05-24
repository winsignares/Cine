from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_asientos = Blueprint("routes_asientos", __name__)
from Model.Funciones import funciones


@routes_asientos.route('/indexAsientos', methods=['GET'] )
def indexAsientos():
    
    return render_template('/Main/Asientos.html')

