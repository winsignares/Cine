from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_Acerca = Blueprint("routes_Acerca", __name__)


@routes_Acerca.route('/IndexAcercaDe', methods=['GET'] )
def IndexAcercaDe():
    
    return render_template('/Main/IndexAcercaDe.html')