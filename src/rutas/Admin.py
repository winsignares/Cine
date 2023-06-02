from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_Admin = Blueprint("routes_Admin", __name__)


@routes_Admin.route('/indexAdmin', methods=['GET'] )
def indexAdmin():
    return render_template('/Main/IndexAdmin.html')
