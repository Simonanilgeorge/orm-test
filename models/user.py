from sqlalchemy.sql.functions import user
from db import db
import json
from flask import jsonify
import datetime
from sqlalchemy import func
from sqlalchemy.sql import alias,select
# from passlib.apps import custom_app_context as pwd_context


class UserModel(db.Model):
    
    # specify the table name
    __tablename__="users"

    # specify the columns
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    age=db.Column(db.Integer)
    count=db.Column(db.Boolean)
    marks=db.Column(db.Float)
    password_hash=db.Column(db.String(80))
    # date=db.Column(db.Date,default=datetime.datetime.now())

    def __init__(self,name,age,count,marks):
        self.name=name
        self.age=age
        self.count=count
        self.marks=marks


    # method to hash the password
    # this method is called when a new user is registering or when a user changes the password
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    # method to verify the password;method is called when user provides credentials
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
# method to add to db
    @classmethod
    def saveToDb(cls,objects):
       
        # db.session.add(self)  
        db.session.bulk_save_objects(objects)  
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
        
        # print(f"Usermodel class {cls.query}")

        # get table name 
        print(f"__table__ is  {UserModel.__dict__['__table__']}" )
        # using an alias
        st = UserModel.__dict__['__table__'].alias("u")
        print(db.session.query(st.c.name).all())
        print(db.session.query(st).filter(st.c.age==(db.session.query(func.max(UserModel.age)).filter(UserModel.name==st.c.name))).all())
        # print(db.session.query(st).filter(UserModel.age==(db.session.query(func.max(UserModel.age)).filter(UserModel.name==st.name))))
        # to print the query
        # print("fetch query")
        # print("st:::")
        # print(st.__dict__)
        # using an alias for select statement
       

        # select statement without alias 
        # print(db.session.query(UserModel))


        return db.session.query(UserModel).all()

    @classmethod
    def getTotalMarks(cls):

        marks=db.session.query(func.sum(UserModel.marks)).first()
        return marks

    @classmethod
    def getCount(cls):
        
        # get count 
        # count=db.session.query(UserModel).count()

        # get users with count=False

        users=db.session.query(UserModel).filter(UserModel.count==False).count()
        return users
    @classmethod
    def getSingleUser(cls,ID):
        user=db.session.query(UserModel).filter(UserModel.id==ID).first()
        return user
    # def __str__(self):
    #     return f"name : {self.name}, age : {self.age}"
    # def __repr__(self):
    #     return f"id : {self.id} name : {self.name}, age : {self.age}"
