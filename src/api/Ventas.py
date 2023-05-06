from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Ventas import ventas, ventasSchema

routes_ventas = Blueprint("routes_ventas", __name__)
#Roles
venta_schema = ventasSchema()
ventas_schema = ventasSchema(many=True)

@routes_ventas.route('/indexventa', methods=['GET'] )
def indexventa():
    return "hello world"