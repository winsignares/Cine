from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripMandalorian = Blueprint("routes_DescripMandalorian", __name__)


@routes_DescripMandalorian.route('/indexDescripMandalorian', methods=['GET'] )
def indexDescripMandalorian():
    
    return render_template('/Main/DESCRIPCIONES/DescripMandalorian.html')