from flask import Flask
from os import getenv
from app.configs import migrations, database, auth
from app import routes
from environs import Env
from datetime import timedelta

env = Env()
env.read_env()

def create_app() -> Flask:
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config['JWT_SECRET_KEY'] = getenv('JWT_SECRET_KEY')
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)

    database.init_app(app)
    migrations.init_app(app)
    routes.init_app(app)
    auth.init_app(app)

    return app
