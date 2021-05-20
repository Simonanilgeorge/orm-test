from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserResource
from models.user import UserModel


app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

api=Api(app)


@app.before_first_request
def create_tables():
    # db.drop_all()
    db.create_all()

# add resources
api.add_resource(UserResource,'/users')



if __name__=="__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True,port=6000)