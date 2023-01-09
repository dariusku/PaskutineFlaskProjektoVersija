from flask import Flask
from flask_login import LoginManager
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin.contrib.sqla import ModelView
import os

db = SQLAlchemy()



def create_app():


    basedir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, ' data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='admin', template_mode='bootstrap3')
    from .models import Klientas, Restoranas
    admin.add_view(ModelView(Klientas, db.session))
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

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login.prisijungti'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        if Klientas:
            return Klientas.query.get(int(id))
        elif Restoranas:
            return Restoranas.query.get(int(id))
    return app


def create_db(app):
    if not os.path.exists('Reservation_system/' + 'data.sqlite'):
        db.create_all(app=app)
        print("* Sukurta Db")