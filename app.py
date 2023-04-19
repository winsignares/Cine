from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#importar routes
from api.roles import routes_roles

#Rutas
from rutas.Mainlogin import routes_mainlogin

#ubicacion del api
app.register_blueprint(routes_roles, url_prefix="/api")


#Ubicacion rutas
app.register_blueprint(routes_mainlogin, url_prefix="/fronted")


@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/Main/MainLogin', titles=titulo)

@app.route("/algo")
def otr():
    return "hola Santiago"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    


