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
    # date=db.Column(db.String,default="hello")

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def saveToDb(self):

       
        db.session.add(self)
        # print(query)
        db.session.commit()

# method to delete from db
    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()

# method to convert object to dictionary
    def convert(self):
        data=self.__dict__
        print(data)
        data.pop("_sa_instance_state")
        return data


    @classmethod
    def getUsers(cls):
        
        return UserModel.query.all()
        
    # def __str__(self):
    #     return f"name : {self.name}, age : {self.age}"
    # def __repr__(self):
    #     return f"id : {self.id} name : {self.name}, age : {self.age}"
