from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripCall = Blueprint("routes_DescripCall", __name__)


@routes_DescripCall.route('/indexDescripCall', methods=['GET'] )
def indexDescripCall():
    
    return render_template('/Main/DESCRIPCIONES/DescripCall.html')