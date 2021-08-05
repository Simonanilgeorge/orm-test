from flask_restful import Resource,reqparse
from models.user import UserModel
from models.store import StoreModel
import json
from flask import jsonify


class StoreResource(Resource):
    
    
    parser=reqparse.RequestParser()
    
    parser.add_argument(
        "name",
        type=str,

    )


    
    def get(self):

        stores=StoreModel.getAllStores()
        
        list=[store.convert() for store in stores]

        return {"stores":list}
    

    def post(self):
        data=StoreResource.parser.parse_args()
        print(data)
        name=data["name"]
        print(name)
        store=StoreModel(name)
        store.saveToDb()
        return {"message":"store added"}  
       

  


class SingleStoreResource(Resource):


    


    def get(self,id):
        return {"message":f"single store with id {id} "}
    

