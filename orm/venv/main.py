from peewee import *
# import sqlite3
from pprint import pprint as pp

conn = SqliteDatabase('database.db')

universities = {
    1: "MIT",
    2: "Stanford",
    3: "Harvard",
    4: "Yale",
    5: "Oxford",
    6: "Boston",
    7: "Brown",
}
religions = {
    1: "Christian",
    2: "Islam",
    3: "Buddhism",
    4: "Judaism",
    5: "Hindu",
    6: "Satanism",
}

class Person(Model):
    name = CharField(max_length=50, unique=True,
                     column_name="imya", default="no name",
                     help_text="vvedite syuda imya cheloveka")
    age = IntegerField()
    gender = CharField(max_length=30, default='other')
    education = CharField(max_length=100,
                          choices=universities,
                          help_text="vyberite uni")
    email = CharField(max_length=50)
    phone = CharField(max_length=15)
    job = BooleanField(default=False)
    family = BooleanField(default=False)
    religion = CharField(max_length=20,
                         choices=religions,
                         default="Atheist")
    class Meta:
        database = conn
        table_name = 'person'

conn.create_tables([Person])

# human = Person.create(name="jay", age="33", gender="male",
#                      education=universities[5], email="parkjay@gmail.com", phone="+996883488372",
#                      religion=religions[1])

# human = Person.update(gender="female").where(Person.name == "mariya")
# human.execute()

#
# pp(human.__dict__)
# def print_info():
#     query = Person.select().order_by(Person.id.desc())
#     for item in query:
#         pp(item.__dict__)
# print_info()

human = Person.get(Person.id == 1)
human.delete_instance()
# human = Person.select()
# pp(human)

cur = conn.cursor()
conn.close()
print('ok')
# with sqlite3.connect('database.db') as db:
#     pass