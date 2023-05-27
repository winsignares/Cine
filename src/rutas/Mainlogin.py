from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import usuarios
#Blueprint
routes_mainlogin = Blueprint("routes_mainlogin", __name__)
#Home
@routes_mainlogin.route('/indexMain', methods=['GET'] )
def indexMain():    
    return render_template('/Main/Main.html')
#Login
@routes_mainlogin.route('/indexmainlogin', methods=['GET'] )
def indexmainlogin():
    return render_template('/Main/MainLogin.html')
#Registro - html
@routes_mainlogin.route('/indexmainregistro', methods=['GET'] )
def indexmainregistro():    
    return render_template('/Main/MainRegistro.html')
#Loguear
@routes_mainlogin.route('/validarUsuarioslg', methods=['POST'] )
def validarUsuarioslg():
    email = request.json['correo_electronico']
    password = request.json['contrasena']
    user = usuarios.query.filter_by(correo_electronico=email,contrasena=password).first()
    print("\nEmail:",email,"Password:",password,"\n")
    if user:
        nav = "/fronted/indexMain"
    else:
        nav = "/fronted/indexmainlogin"
    return nav
#Registrar
@routes_mainlogin.route('/validarUsuariosrg', methods=['POST'] )
def validarUsuariosrg():
    print("ok\n")
    nombre = request.json['nombre']
    Rol = request.json['Rol']
    correo_electronico = request.json['correo_electronico']
    contrasena = request.json['contrasena']
    new_user = usuarios(Rol,nombre,correo_electronico,contrasena)
    db.session.add(new_user)
    db.session.commit()
    print("ok")
    return "/fronted/indexmainlogin"