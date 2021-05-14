from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False



api=Api(app)
