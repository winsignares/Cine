from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#importar routes del API
from api.Pelicula import routes_peliculas
from api.Roles import routes_roles
from api.Salas import routes_salas
from api.Usuarios import routes_usuarios
from api.Funciones import routes_funciones
from api.Compra import routes_compra
from api.Asientos import routes_Iasiento
from api.Tickets import routes_tickets


#Rutas
from rutas.Mainlogin import routes_mainlogin
from rutas.index import routes_index
from rutas.Asientos import routes_asientos
from rutas.Admin import routes_Admin

#ubicacion del api
app.register_blueprint(routes_compra, url_prefix="/api")
app.register_blueprint(routes_funciones, url_prefix="/api")
app.register_blueprint(routes_peliculas, url_prefix="/api")
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_salas, url_prefix="/api")
app.register_blueprint(routes_Iasiento, url_prefix="/api")
app.register_blueprint(routes_usuarios, url_prefix="/api")
app.register_blueprint(routes_tickets, url__prefix="/api")

#Ubicacion rutas
app.register_blueprint(routes_mainlogin, url_prefix="/fronted")
app.register_blueprint(routes_index, url_prefix="/fronted")
app.register_blueprint(routes_asientos,url_prefix="/fronted")
app.register_blueprint(routes_Admin, url_prefix="/fronted")

@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/Main/MainLogin.html', titles=titulo)

@app.route("/Dainer")
def otr():
    return "Dainer"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    


