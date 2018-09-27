import psycopg2
from app.models.tables import commands


class Database_connection():
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='ruiru' user='ruiru' password='ruiru' host='localhost' port='5432'"
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print("CANNOT CONNECT TO DATABASE INVALID DATABASE URL")

    def create_tables(self):
        for command in commands:
            self.cursor.execute(command)
