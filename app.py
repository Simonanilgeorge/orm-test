from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserResource
from models.user import UserModel
from flask_cors import CORS
from db import db
    


app=Flask(__name__)
api=Api(app)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False



db.init_app(app)


@app.before_first_request
def create_tables():
    # db.drop_all()
    db.create_all()

# add resources
api.add_resource(UserResource,'/users')



if __name__=="__main__":

    # app.run(host='0.0.0.0',port=5000)
    app.run(host='0.0.0.0',port=5000,debug=True)