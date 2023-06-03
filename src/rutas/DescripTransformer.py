from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripTransformer = Blueprint("routes_DescripTransformer", __name__)


@routes_DescripTransformer.route('/indexDescripTransformer', methods=['GET'] )
def indexDescripTransformer():
    
    return render_template('/Main/DESCRIPCIONES/DescripTransformer.html')