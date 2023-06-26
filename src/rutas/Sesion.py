from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template

@app.route('/')
def index():
    token = request.headers.get('Authorization')  # Obtener el token del encabezado de autorización
    # Resto del código para renderizar la página web
    return render_template('indexMain', token=token)

