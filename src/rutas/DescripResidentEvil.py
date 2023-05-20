from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripResidentEvil = Blueprint("routes_DescripResidentEvil", __name__)


@routes_DescripResidentEvil.route('/indexDescripResidentEvil', methods=['GET'] )
def indexDescripResidentEvil():
    
    return render_template('/Main/DESCRIPCIONES/DescripResidentEvil.html')