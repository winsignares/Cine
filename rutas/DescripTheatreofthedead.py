from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripTheatreofthedead = Blueprint("routes_DescripTheatreofthedead", __name__)


@routes_DescripTheatreofthedead.route('/indexDescripTheatreofthedead', methods=['GET'] )
def indexDescripTheatreofthedead():
    
    return render_template('/Main/DESCRIPCIONES/DescripTheatreofthedead.html')