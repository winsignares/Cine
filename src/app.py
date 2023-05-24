from flask import Flask,  redirect, request, jsonify, json, session, render_template
from config.db import db, app, ma

#importar routes del API
from api.Roles import routes_roles
from api.peliculas import Blueprint

#Rutas
from rutas.Mainlogin import routes_mainlogin
from rutas.index import routes_index
from rutas.descripcion import routes_Descripcion
from rutas.DescripStranger import routes_DescripcionStranger
from rutas.Descripbloodshot import routes_Descripbloodshot
from rutas.DescripMandavision import routes_DescripMandavision
from rutas.DescripInifinitytrain import routes_DescripInifinitytrain
from rutas.DescripSupergil import routes_DescripSupergil
from rutas.DescripCapitanmarvel import routes_DescripCapitanmarvel
from rutas.DescripTheDarkKnight import routes_DescripTheDarkKnight
from rutas.DescripTheatreofthedead import routes_DescripTheatreofthedead
from rutas.DescripTransformer import routes_DescripTransformer
from rutas.DescripResidentEvil import routes_DescripResidentEvil
from rutas.DescripHunterKiller import routes_DescripHunterKiller
from rutas.DescripCall import routes_DescripCall
from rutas.DescripPenthouses import routes_DescripPenthouses
from rutas.DescripStarTrek import routes_DescripStarTrek
from rutas.DescripDragonBallSuper import routes_DescripDragonBallSuper
from rutas.DescripMandalorian import routes_DescripMandalorian
from rutas.Admin import routes_Admin


#ubicacion del api
app.register_blueprint(routes_roles, url_prefix="/api")


#Ubicacion rutas
app.register_blueprint(routes_mainlogin, url_prefix="/fronted")
app.register_blueprint(routes_index, url_prefix="/fronted")
app.register_blueprint(routes_Descripcion, url_prefix="/fronted")
app.register_blueprint(routes_DescripcionStranger, url_prefix="/fronted")
app.register_blueprint(routes_Descripbloodshot, url_prefix="/fronted")
app.register_blueprint(routes_DescripMandavision, url_prefix="/fronted")
app.register_blueprint(routes_DescripInifinitytrain, url_prefix="/fronted")
app.register_blueprint(routes_DescripSupergil, url_prefix="/fronted")
app.register_blueprint(routes_DescripCapitanmarvel, url_prefix="/fronted")
app.register_blueprint(routes_DescripTheDarkKnight, url_prefix="/fronted")
app.register_blueprint(routes_DescripTheatreofthedead, url_prefix="/fronted")
app.register_blueprint(routes_DescripTransformer, url_prefix="/fronted")
app.register_blueprint(routes_DescripResidentEvil, url_prefix="/fronted")
app.register_blueprint(routes_DescripHunterKiller, url_prefix="/fronted")
app.register_blueprint(routes_DescripCall,url_prefix="/fronted" )
app.register_blueprint(routes_DescripPenthouses,url_prefix="/fronted")
app.register_blueprint(routes_DescripStarTrek,url_prefix="/fronted")
app.register_blueprint(routes_DescripDragonBallSuper,url_prefix="/fronted")
app.register_blueprint(routes_DescripMandalorian,url_prefix="/fronted")
app.register_blueprint(routes_Admin,url_prefix="/fronted")


@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/Main/MainLogin.html', titles=titulo)

@app.route("/funciona?")
def otr():
    return "¡Hola!"


# Datos de la tabla de Editoriales
if __name__ == '__main__':
    # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    


