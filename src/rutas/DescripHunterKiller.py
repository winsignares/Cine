from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_DescripHunterKiller = Blueprint("routes_DescripHunterKiller", __name__)


@routes_DescripHunterKiller.route('/indexDescripHunterKiller', methods=['GET'] )
def indexDescripHunterKiller():
    
    return render_template('/Main/DESCRIPCIONES/DescripHunterKiller.html')