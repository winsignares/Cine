from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripInifinitytrain = Blueprint("routes_DescripInifinitytrain", __name__)


@routes_DescripInifinitytrain.route('/indexDescripInifinitytrain', methods=['GET'] )
def indexDescripcionDescripcio():
    
    return render_template('/Main/DESCRIPCIONES/DescripInifinitytrain.html')