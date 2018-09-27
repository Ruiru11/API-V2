from flask import Flask
from .config import config_by_name
from app.models.Database import Database_connection
from app.views.orders import mod_orders
from app.views.users import mod_users
from app.views.menus import mod_menus

db=Database_connection()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db
    app.register_blueprint(mod_orders)
    app.register_blueprint(mod_users)
    app.register_blueprint(mod_menus)
    return app
