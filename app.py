from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#importar routes
api

#Rutas
from rutas.Mainlogin import routes_mainlogin

#ubicacion del api
app.register_blueprint(routes_routes_mainlogin, urlprefix="/fronted")


#Ubicacion rutas
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
    


