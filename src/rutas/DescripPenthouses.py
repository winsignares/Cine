from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripPenthouses = Blueprint("routes_DescripPenthouses", __name__)


@routes_DescripPenthouses.route('/indexDescripPenthouses', methods=['GET'] )
def indexDescripPenthouses():
    
    return render_template('/Main/DESCRIPCIONES/DescripPenthouses.html')