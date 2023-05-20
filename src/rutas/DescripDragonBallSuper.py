from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripDragonBallSuper = Blueprint("routes_DescripDragonBallSuper", __name__)


@routes_DescripDragonBallSuper.route('/indexDescripDragonBallSuper', methods=['GET'] )
def indexDescripDragonBallSuper():
    
    return render_template('/Main/DESCRIPCIONES/DescripDragonBallSuper.html')