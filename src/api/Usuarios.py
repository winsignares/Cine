from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from flask import Flask, Blueprint, redirect, request, jsonify, json, session, render_template
from Model.Usuarios import usuarios,usuariosSchema

routes_roles = Blueprint("routes_usuarios", __name__)

#Roles
usuario_schema = usuariosSchema()
usuarios_schema = usuariosSchema(many=True)


@routes_roles.route('/indexusuarios', methods=['GET'] )
def indexusuarios():
    return "hello world"

@app.route('/Usuarios', methods=['GET'])
def usuarios():    
    returnall = usuarios.query.all()
   
    resultado_usuarios = usuarios_schema.dump(returnall)
    return jsonify(resultado_usuarios)

@app.route('/save_Users', methods=['POST'] )
def guardar_Users():
    Usuarios = request.json['full_name,Email,password,telefono,especialidad,jornada,direccion,id_roles']
    print(Usuarios)
    new_Users = usuarios(Usuarios)
    db.session.add(new_Users)
    db.session.commit()
    return redirect('/Usuarios')