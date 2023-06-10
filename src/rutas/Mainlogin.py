from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import usuarios
# Blueprint
routes_mainlogin = Blueprint("routes_mainlogin", __name__)
# Home


@routes_mainlogin.route('/indexMain', methods=['GET'])
def indexMain():
    return render_template('/Main/IndexMain.html')
# Login


@routes_mainlogin.route('/indexmainlogin', methods=['GET'])
def indexmainlogin():
    return render_template('/Main/IndexMainLogin.html')
# Registro - html


@routes_mainlogin.route('/indexmainregistro', methods=['GET'])
def indexmainregistro():
    return render_template('/Main/IndexMainRegistro.html')
# Loguear


@routes_mainlogin.route('/validarUsuarioslg', methods=['POST'])
def validarUsuarioslg():
    email = request.json['correo_electronico']
    password = request.json['contrasena']
    user = usuarios.query.filter_by(
        correo_electronico=email, contrasena=password).first()
    print("\nEmail:", email, "Password:", password, "\n")
    print("\nuser response:", type(user))
    userid = usuarios.Rol
    if not user:
        nav = "/fronted/indexmainlogin"
    elif user.Rol == "cliente":
        nav = "/fronted/indexMain"
    elif user.Rol == "admin":
        nav = "/fronted/indexAdmin"

    data = {
        'userid': userid,
        'nav': nav
    }

    response = jsonify(data)
    return response
# Registrar


@routes_mainlogin.route('/validarUsuariosrg', methods=['POST'])
def validarUsuariosrg():
    print("ok\n")
    nombre = request.json['nombre']
    Rol = request.json['Rol']
    correo_electronico = request.json['correo_electronico']
    contrasena = request.json['contrasena']
    new_user = usuarios(Rol, nombre, correo_electronico, contrasena)
    db.session.add(new_user)
    db.session.commit()
    print("ok")
    return "/fronted/indexmainlogin"
    
@routes_mainlogin.route('/getuser', methods=['GET'])
def getUserById():
    userId = request.json['userid']
    user = usuarios.query.filter_by(id=userId).first()
    print("Data", user.Rol)
    userFound = {
        'userid': user.id,
        'rol': user.Rol,
        'name': user.nombre,
        'email': user.correo_electronico
    }
    
    response = jsonify(userFound)
    return response