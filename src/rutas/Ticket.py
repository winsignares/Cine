from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_CTicket = Blueprint("routes_CTicket", __name__)


@routes_CTicket.route('/CTicket', methods=['GET'] )
def indexTicket():
    
    return render_template('/Main/IndexTicket.html')