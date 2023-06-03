from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripMandavision = Blueprint("routes_DescripMandavision", __name__)


@routes_DescripMandavision.route('/indexDescripMandavision', methods=['GET'] )
def indexDescripcionDescripcio():
    
    return render_template('/Main/DESCRIPCIONES/DescripMandavision.html')