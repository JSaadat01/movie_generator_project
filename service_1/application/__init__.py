from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@35.197.207.20:3306/project"
db = SQLAlchemy(app)

from application import routes