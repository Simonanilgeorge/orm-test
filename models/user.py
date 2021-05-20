from db import db
import json
from flask import jsonify
import datetime
from sqlalchemy import func


class UserModel(db.Model):
    
    # specify the table name
    __tablename__="users"

    # specify the columns
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    age=db.Column(db.Integer)
    count=db.Column(db.Boolean)
    # date=db.Column(db.Date,default=datetime.datetime.now())

    def __init__(self,name,age,count):
        self.name=name
        self.age=age
        self.count=count

    def saveToDb(self):

       
        db.session.add(self)
       
        db.session.commit()

# method to delete from db
    def deleteFromDb(self):
        db.session.delete(self)
        db.session.commit()

# method to convert object to dictionary
    def convert(self):
        data=self.__dict__
        # print(data)
        data.pop("_sa_instance_state")
        
        return data


    @classmethod
    def getUsers(cls):
        
        print(f"Usermodel class {cls.query}")
        return db.session.query(UserModel).all()

    @classmethod
    def getCount(cls):
        
        # get count 
        # count=db.session.query(UserModel).count()

        # get users with count=true
        users=db.session.query(UserModel).filter(UserModel.count==False).all()
        return users
        
    # def __str__(self):
    #     return f"name : {self.name}, age : {self.age}"
    # def __repr__(self):
    #     return f"id : {self.id} name : {self.name}, age : {self.age}"
