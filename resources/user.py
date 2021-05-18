from flask_restful import Resource,reqparse
from models.user import UserModel
import json
from flask import jsonify

class UserResource(Resource):

    parser=reqparse.RequestParser()
 
    # add arguments using parser

    parser.add_argument(
        "name",
        type=str
    )
    parser.add_argument(
        "age",
        type=int
    )


    def post(self):

        # get the arguments using parser
        
        data=UserResource.parser.parse_args()
        user=UserModel(data["name"],data["age"])
        # print(f"user : {json.dumps(user.__dict__)}")
        print(f"user : {jsonify(user)}")
        print()
        user.saveToDb()
        return data
    
    def get(self):
        
        data=UserModel.getUsers()
        list=[UserResource.convert(data) for data in data]        
        return json.dumps(list,sort_keys=True)
    
    def delete(self):
        return 
    
    @classmethod
    def convert(cls,data):
        data=data.__dict__
        data.pop("_sa_instance_state")
        return data

