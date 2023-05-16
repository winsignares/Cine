from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripcionStranger = Blueprint("routes_DescripcionStranger", __name__)


@routes_DescripcionStranger.route('/indexDescripcionDescripcion', methods=['GET'] )
def indexDescripcionDescripcion():
    
    return render_template('/Main/DESCRIPCIONES/DescripStranger.html')