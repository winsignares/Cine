from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import usuarios
routes_mainlogin = Blueprint("routes_mainlogin", __name__)


@routes_mainlogin.route('/indexmainlogin', methods=['GET'] )
def indexmainlogin():
    
    return render_template('/Main/MainLogin.html')
#Loguear
@routes_mainlogin.route('/validarUsuarioslg', methods=['POST'] )
def validarUsuarioslg():
    
    email = request.json['email']
    password = request.json['password']
    user = usuarios.query.filter_by(correo_electronico=email,contrasena=password).first()
    print("\nEmail:",email,"Password:",password)
    
    if user:
        print("\nPaso...\n")
        #response_body = {'message':'OK'}
        nav = "/fronted/indexMain"
    else:
        #response_body = {'message':'Invalido'}
        nav = "/fronted/indexmainlogin"

    return nav

@routes_mainlogin.route('/validarUsuariosrg', methods=['POST'] )
def validarUsuariosrg():

    nombre = request.form['nombre']
    correo_electronico = request.form['correo_electronico']
    contrasena = request.form['contrasena']
    print("\n",nombre,"\n")
    new_user = usuarios(nombre,correo_electronico,contrasena)
    db.session.add(new_user)
    db.session.commit()
    return "ok"