from flask_restful import Resource,reqparse
from models.user import UserModel
from models.store import StoreModel
import json
from flask import jsonify


class StoreResource(Resource):
    
    def get(self):

        return {"message":"All stores"}
    

    def post(self):
        data=SingleStoreResource.parser.parse_args()
        name=data["name"]
        store=StoreModel(name)
        store.saveToDb()
        return {"message":"store added"}    


class SingleStoreResource(Resource):

    parser=reqparse.RequestParser()
    
    parser.add_argument(
        "name",
        type=str,
        action="append"
    )


    def get(self,id):
        return {"message":f"single store with id {id} "}
    

