from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_registro = Blueprint("routes_registro", __name__)


@routes_registro.route('/indexmainregistro', methods=['GET'] )
def indexmainregistro():
    
    return render_template('/Main/MainRegistro.html')