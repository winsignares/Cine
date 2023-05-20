from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripTheDarkKnight = Blueprint("routes_DescripTheDarkKnight", __name__)


@routes_DescripTheDarkKnight.route('/indexDescripTheDarkKnight', methods=['GET'] )
def indexDescripTheDarkKnight():
    
    return render_template('/Main/DESCRIPCIONES/DescripTheDarkKnight.html')