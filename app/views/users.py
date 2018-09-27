from flask import Blueprint
from flask_restful import reqparse
from app.controllers.users import Users

mod_users = Blueprint('users', __name__, url_prefix='/api/v2')

usr = Users()

@mod_users.route('/signup', methods=['POST'])
def create_user():
    parser = reqparse.RequestParser()
    parser.add_argument('id',type=int, location="json")
    parser.add_argument('email',type=str, location="json")
    parser.add_argument('address',type=str,location="json")
    parser.add_argument('password',type=str,location="json")
    parser.add_argument('username',type=str,location="json")
    data = parser.parse_args()

    return usr.create_user(data)

@mod_users.route('/users', methods=['GET'])
def get_users():
    return usr.get_users()