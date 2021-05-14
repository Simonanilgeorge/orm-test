from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserResource


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

api=Api(app)

# add resources
api.add_resource(UserResource,'/users')

if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True,port=6000)