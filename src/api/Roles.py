
from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask,  redirect, request, jsonify, json, session, render_template

from Model.RolesUsuario import RolesUsuarios, RolesSchema

routes_roles = Blueprint("routes_rol", __name__)
#Roles
rolesusuario_schema = RolesSchema()
rolesusuarios_schema = RolesSchema(many=True)

@routes_roles.route('/indexroles', methods=['GET'] )
def indexRoles():
    
    return "Hola Mundo!!"