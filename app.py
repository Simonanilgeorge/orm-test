from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserResource
from resources.register import RegisterResource
from resources.store import StoreResource,SingleStoreResource

from models.user import UserModel
from flask_cors import CORS
from db import db
import logging
    


app=Flask(__name__)
api=Api(app)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


# get logs for gunicorn
# gunicorn_error_logger = logging.getLogger('gunicorn.error')
# app.logger.handlers.extend(gunicorn_error_logger.handlers)
# app.logger.setLevel(logging.DEBUG)


db.init_app(app)


@app.before_first_request
def create_tables():
    # db.drop_all()
    db.create_all()

# add resources
api.add_resource(UserResource,'/api/users')
api.add_resource(RegisterResource,'/api/register')
api.add_resource(StoreResource,'/api/stores')
api.add_resource(SingleStoreResource,"/api/stores/<string:id>")



if __name__=="__main__":

    # app.run(host='0.0.0.0',port=5000)
    
    app.run(host='0.0.0.0',port=5000,debug=True)