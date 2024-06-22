from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import os
from flask_jwt_extended import JWTManager


load_dotenv




db = SQLAlchemy()

app = Flask(__name__)

jwt = JWTManager(app)


app.secret_key = environ.get("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = environ.get("JWT_SECRET_KEY")
app.config['SQLACHEMY_ECHO'] = environ.get("SQLALCHEMT_ECHO")

db.init_app(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
migrate = Migrate(app, db)
