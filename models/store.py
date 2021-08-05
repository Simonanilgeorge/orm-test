from sqlalchemy.sql.functions import user
from db import db
import json
from flask import jsonify
import datetime
from sqlalchemy import func
from sqlalchemy.sql import alias,select



class StoreModel(db.Model):

    __tablename__="stores"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))

    def __init__(self,name):
        self.name=name

    def saveToDb(self):

        db.session.add(self)
        db.session.commit()
    



