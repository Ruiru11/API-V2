from flask import jsonify, make_response
from app.models.Database import Database_connection
import psycopg2

class Users(object):
    def __init__(self):
        self.connection = Database_connection()
    
    def create_user(self, data):
        try:
            self.connection.cursor.execute("""INSERT INTO users(id, email, username, password, address)
            VALUES(%s,%s,%s, %s, %s);""",
            (data['id'], data['email'], data['username'], data['password'],data['address'] ))
            print("Inserting data into users")
            response_object = {
                "status":"pass",
                "message":"user added succesfuly"
            }
            return(make_response(jsonify(response_object)))
        except (Exception, psycopg2.DatabaseError) as error:
            print("Entry with same id already exists or wrong format used",error)
            response_object = {
                "status":"fail",
                "message":"Entry with same id already exists or wrong format used"
            }
            return(make_response(jsonify(response_object)))
    
    def get_users(self):
        self.connection.cursor.execute("""SELECT * FROM users""")
        news = self.connection.cursor.fetchall()
        for new in news:
            return(jsonify(news))