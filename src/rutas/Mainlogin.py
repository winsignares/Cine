from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
from Model.Usuarios import usuarios
from common.token import *
#Blueprint
routes_mainlogin = Blueprint("routes_mainlogin", __name__)
#Home
@routes_mainlogin.route('/indexMain', methods=['GET'] )
def indexMain():    
    return render_template('/Main/IndexMain.html')

#Login
@routes_mainlogin.route('/indexmainlogin', methods=['GET'] )
def indexmainlogin():
    return render_template('/Main/IndexMainLogin.html')

#Registro - html
@routes_mainlogin.route('/indexmainregistro', methods=['GET'] )
def indexmainregistro():    
    return render_template('/Main/IndexMainRegistro.html')
#Loguear

SECRET_KEY = "200207"

@routes_mainlogin.route('/validarUsuarioslg', methods=['POST'])
def validarUsuarioslg():
    email = request.json['correo_electronico']
    password = request.json['contrasena']
    user = usuarios.query.filter_by(correo_electronico=email, contrasena=password).first()
    print("\nEmail:", email, "Password:", password, "\n")
    
    if user:
        # Generar el token con datos del usuario
        token = generar_token(email)
        # Guardar el token en la base de datos
        user.token = token
        db.session.commit()
        # Redirigir al usuario a la ubicación indicada con el token como parámetro
        nav = "/fronted/indexMain?token=" + token
    else:
        nav = "/fronted/indexmainlogin"

    data = {
        'nav': nav
    }
    return jsonify(data)
def generar_token(email):
    # Obtener la fecha y hora actual
    now = datetime.utcnow()
    
    # Establecer la fecha de expiración del token (por ejemplo, 1 hora desde ahora)
    expiration = now + timedelta(hours=1)
    
    # Crear el payload del token con el correo electrónico y la fecha de expiración
    payload = {
        "email": email,
        "exp": expiration
    }
    
    # Generar el token utilizando la clave secreta y el algoritmo HS256
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    return token

#Registrar
@routes_mainlogin.route('/saveUsuariosrg', methods=['POST'])
def saveUsuariosrg():
    nombre = request.json['nombre']
    Rol = request.json['Rol']
    correo_electronico = request.json['correo_electronico']
    contrasena = request.json['contrasena']
    
    # Generar el token con el correo electrónico como información adicional
    token = generar_token(correo_electronico)
    
    # Crear una nueva instancia de usuarios con los datos proporcionados y el token generado
    new_user = usuarios(Rol, nombre, correo_electronico, contrasena, token)
    
    # Agregar el nuevo usuario a la sesión y guardar los cambios en la base de datos
    db.session.add(new_user)
    db.session.commit()
    
    # Redirigir al usuario a la ubicación indicada
    return "/fronted/indexmainlogin"

def generar_token(correo_electronico):
    now = datetime.utcnow()
    expiration = now + timedelta(hours=1)
    
    payload = {
        "email": correo_electronico,
        "exp": expiration
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    return token


@routes_mainlogin.route('/obtener_nombre_usuario', methods=['GET'])
def obtener_nombre_usuario():
    token = request.args.get('token')  # Obtener el token de la solicitud GET

    # Realizar una consulta a la base de datos para encontrar el registro con el token proporcionado
    usuario = usuarios.query.filter_by(token=token).first()

    if usuario:
        nombre_usuario = usuario.nombre  # Obtener el nombre del usuario

        return jsonify({'nombre_usuario': nombre_usuario})
    else:
        return jsonify({'error': 'Token de usuario inválido'})