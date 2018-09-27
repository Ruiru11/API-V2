import os
import psycopg2

from flask_script import Manager

from app import create_app, db

app = create_app(os.getenv('ENV') or 'dev')

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run()

@manager.command
def init_db():
    try:
        print("CREATING TABLES")
        db.create_tables()
    except (Exception, psycopg2.DatabaseError) as error:
        print("FAILED TO CREATE TABLES", error)


if __name__ == '__main__':
    manager.run()
