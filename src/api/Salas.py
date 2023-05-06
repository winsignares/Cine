from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from common.token import *
from flask import Flask,  redirect, request, jsonify, json, session, render_template
from Model.Salas import salas, salasSchema

routes_salas = Blueprint("routes_salas", __name__)
#Roles
sala_schema = salasSchema()
salas_schema = salasSchema(many=True)

@routes_salas.route('/indexsalas', methods=['GET'] )
def indexsalas():
    return "hello world"