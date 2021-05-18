from db import db
import json
from flask import jsonify


class UserModel(db.Model):
    
    # specify the table name
    __tablename__="users"

    # specify the columns
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    age=db.Column(db.Integer)

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def saveToDb(self):

        print(f"self : {self}")
        db.session.add(self)
        db.session.commit()


    @classmethod
    def getUsers(cls):
        
        return UserModel.query.all()
        
    def __str__(self):
        return f"name : {self.name}, age : {self.age}"
    def __repr__(self):
        return f"id : {self.id} name : {self.name}, age : {self.age}"
