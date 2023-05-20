from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripSupergil = Blueprint("routes_DescripSupergil", __name__)


@routes_DescripSupergil.route('/indexDescripSupergil', methods=['GET'] )
def indexDescripSupergil():
    
    return render_template('/Main/DESCRIPCIONES/DescripSupergil.html')