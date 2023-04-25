from flask import Flask
from flask_sqlAlchemy import SQLAlchemy
from flask_Marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/cine'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "cine"

db = SQLAlchemy(app)

ma = Marshmallow(app)