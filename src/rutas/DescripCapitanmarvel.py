from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripCapitanmarvel = Blueprint("routes_DescripCapitanmarvel", __name__)


@routes_DescripCapitanmarvel.route('/indexDescripCapitanmarvel', methods=['GET'] )
def indexDescripCapitanmarvel():
    
    return render_template('/Main/DESCRIPCIONES/DescripCapitanmarvel.html')