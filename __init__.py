from flask import Flask
from flask_login import LoginManager, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()



def create_app():


    basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, ' data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    migrate = Migrate(app, db)
    migrate.init_app(app,db)

    from Reservation_system.restaurant_auth import r_auth
    from Reservation_system.restaurant import restaurant
    from Reservation_system.login import login
    from Reservation_system.client import client
    from Reservation_system.client_auth import c_auth
    from Reservation_system.base_routes import base_routes
    app.register_blueprint(base_routes, url_prefix='/')
    app.register_blueprint(c_auth, url_prefix='/')
    app.register_blueprint(client, url_prefix='/')
    app.register_blueprint(r_auth, url_prefix='/')
    app.register_blueprint(restaurant, url_prefix='/')
    app.register_blueprint(login, url_prefix='/')
    from .models import Klientas,Restoranas
    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login.prisijungti'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Klientas.query.get(int(id))

    @login_manager.user_loader
    def load_r_user(id):
        return Restoranas.query.get(int(id))

    return app


def create_db(app):
    if not os.path.exists('Reservation_system/' + 'data.sqlite'):
        db.create_all(app=app)
        print("* Sukurta Db")