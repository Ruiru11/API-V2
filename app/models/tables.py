h1 = (
    """
CREATE TABLE IF NOT EXISTS MEALS(
name VARCHAR(20) NOT NULL,
description VARCHAR(30) NOT NULL,
meal_id INTEGER PRIMARY KEY
)
""")

h3 = (
    """
CREATE TABLE IF NOT EXISTS ORDERS(
order_id INTEGER PRIMARY KEY,
status VARCHAR (20),
user_id INTEGER ,
cost INTEGER NOT NULL,
description VARCHAR NOT NULL,
item VARCHAR NOT NULL
)
""")

h2 = ("""
CREATE TABLE IF NOT EXISTS USERS(
id serial primary key,
username VARCHAR(10) NOT NULL,
email VARCHAR(20) NOT NULL,
password VARCHAR NOT NULL,
address VARCHAR(20) NOT NULL
)
""")

h4 = ("""
CREATE TABLE IF NOT EXISTS CATEGORY(
category_id INTEGER PRIMARY KEY,
name VARCHAR(15) NOT NULL,
description VARCHAR(20) NOT NULL
)
""")

commands = [h1, h2, h3, h4]
