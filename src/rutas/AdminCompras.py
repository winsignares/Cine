from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_AdminC = Blueprint("routes_AdminC", __name__)


@routes_AdminC.route('/indexAdminC', methods=['GET'] )
def indexAdminC():
    
    return render_template('/PeliculasWeb-main/AdminCompras.html')