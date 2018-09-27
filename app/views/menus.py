from flask import Blueprint
from flask_restful import reqparse
from app.controllers.menus import Menus

mod_menus = Blueprint('menus', __name__, url_prefix='/api/v2')

mnu = Menus()

@mod_menus.route('/menus', methods=['POST'])
def create_menu():
    parser = reqparse.RequestParser()
    parser.add_argument('meal_id', type=int, location='json')
    parser.add_argument('name', type=str, location='json')
    parser.add_argument('description', type=str, location='json')
    data = parser.parse_args()

    return mnu.create_menu(data)

@mod_menus.route('/menus', methods=['GET'])
def get_menu():
    return mnu.get_menu()


@mod_menus.route('/menus/<int:id>', methods=['GET'])
def get_menus(id):
    return mnu.get_menus(id)