from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_asientos = Blueprint("routes_Admin", __name__)


@routes_asientos.route('/indexAdmin', methods=['GET'] )
def indexAdmin():
    
    return render_template('/Main/Admin.html')