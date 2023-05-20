from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_Descripbloodshot = Blueprint("routes_Descripbloodshot", __name__)


@routes_Descripbloodshot.route('/indexDescripbloodshot', methods=['GET'] )
def indexDescripcionDescripcio():
    
    return render_template('/Main/DESCRIPCIONES/Descripbloodshot.html')