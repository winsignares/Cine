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
            # Obtener el rol del usuario desde la tabla tblusuarios
        rol_usuario = user.id_roles

        if rol_usuario == 1:
            # Establecer la variable de sesión para ocultar la parte del menú correspondiente
            session['hide_dashboard'] = True
        else:
            session['hide_dashboard'] = False
    else:
        # Si el usuario no es válido, establecer la variable de sesión para mostrar el menú completo
        session['hide_dashboard'] = False

    
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
@routes_mainlogin.route('/guardaruser', methods=['POST'])
def save_user():
    fullname = request.form['fullname']
    fullrol = request.form['fullrol']
    fullcorreo = request.form['fullcorreo']
    fullpassword = request.form['fullpassword']

    # Verificar si el ID ya existe en la base de datos
    existing_user = usuarios.query.filter_by(correo_electronico=fullcorreo).first()
    if existing_user:
        #aqui hago el validar, es decir si ya hay un dato, automaticamente no lo guardar y me muestra un mensaje
        response_body = {
            'message': 'El Correo ya está registrado'
        }
        
        status = 400
        headers = {'Content-Type': 'application/json'}
        return jsonify(response_body), status, headers


    new_user = usuarios(nombre= fullname, Rol=fullrol, correo_electronico=fullcorreo, contrasena=fullpassword)
    db.session.add(new_user)
    db.session.commit()

    response_body = {
        'message': 'Registro guardado exitosamente'
    }
    status = 200
    headers = {'Content-Type': 'application/json'}

    return jsonify(response_body), status, headers
