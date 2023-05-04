from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Usuarios import usuarios,usuariosSchema

routes_usuarios = Blueprint("routes_usuarios", __name__)

#Roles
usuario_schema = usuariosSchema()
usuarios_schema = usuariosSchema(many=True)


@routes_usuarios.route('/indexusuarios', methods=['GET'] )
def indexusuarios():
    return "hello world"

@app.route('/Usuarios', methods=['GET'])
def usuarios():    
    returnall = usuarios.query.all()
   
    resultado_usuarios = usuarios_schema.dump(returnall)
    return jsonify(resultado_usuarios)

@app.route('/save_Users', methods=['POST'] )
def guardar_Users():
    Usuarios = request.json['id,id_roles_usuarios,Nombre,Correo_electronico,Contraseña']
    print(Usuarios)
    new_Users = usuarios(Usuarios)
    db.session.add(new_Users)
    db.session.commit()
    return redirect('/Usuarios')