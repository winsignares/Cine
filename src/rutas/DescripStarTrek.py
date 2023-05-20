from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripStarTrek = Blueprint("routes_DescripStarTrek", __name__)


@routes_DescripStarTrek.route('/indexDescripStarTrek', methods=['GET'] )
def indexDescripStarTrek():
    
    return render_template('/Main/DESCRIPCIONES/DescripStarTrek.html')