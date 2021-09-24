import psycopg2
from random import randchoice as rd
from random import randrange as rr
from pprint import pprint as pp
conn = psycopg2.connect(
    dbname='frunze',
    user='aibebk',
    password='123',
    host='localhost',
    port='5432'
)
curs = conn.cursor('')


"""
curs.execute("CREATE TABLE customer("+
            "id SERIAL PRIMARY KEY,"+
            "name VARCHAR NOT NULL,"+
            "phone VARCHAR UNIQUE,"+
            "email VARCHAR)")
"""
curs.execute("CREATE TABLE product("+
            "id SERIAL PRIMARY KEY,"+
            "name VARCHAR NOT NULL,"+
            "description TEXT"+
            "price INT)")

curs.execute("CREATE TABLE product_photo("+
            "id SERIAL PRIMARY KEY,"+
            "url VARCHAR NOT NULL,"+
            "product_id INTEGER REFERENCES product(id))")

curs.execute("CREATE TABLE cart("+
            "id SERIAL PRIMARY KEY,"+
            "customer_id INTEGER REFERENCES customer(id)")


curs.execute("CREATE TABLE cart_photo("+
            "id SERIAL PRIMARY KEY,"+
            "product_id INTEGER REFERENCES product(id)"+
            "customer_id INTEGER REFERENCES cart(id)")

products =["iphone","nokia","xiaomi","huawei","macbook"]
descriptions = 'this is descriptions'

curs.execute("INSERT INTO product"+
            'name,'+
            'description'+
            "price)"+
            "VALUES("+
            f"{rd(products)},"+
            "description,"+
            f"{rr(1.10000000)}")

curs.execute("INSERT INTO product"+
            'name,'+
            'description'+
            "price)"+
            "VALUES("+
            f"{rd(products)},"+
            "description,"+
            f"{rr(1.10000000)}")


curs.execute("SELECT * FROM product")
record = curs.fetchall()
pp(record)