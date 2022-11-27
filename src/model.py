from src.extension.database import db 
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(35),unique=True,nullable=False)
    email = db.Column(db.String(35),unique=True,nullable=False)
    password = db.Column(db.String(250),nullable=False)
    isAdmin = db.Column(db.Boolean,default=False,nullable=False)

"""
class Student(db.Model):
    pass 

class Teacher(db.Model):
    pass 

class Room(db.Model):
    pass 

class Course(db.Model):
    pass

class Subject(db.Model):
    pass 

class Payment(db.Model):
    pass 
"""