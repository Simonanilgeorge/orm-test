from flask_restful import Resource,reqparse
from models.user import UserModel
import json
from flask import jsonify

class UserResource(Resource):

    parser=reqparse.RequestParser()
 
    # add arguments using parser

    # parser.add_argument(
    #     "name",
    #     type=str
    # )
    # parser.add_argument(
    #     "age",
    #     type=int
    # )

    parser.add_argument(
        "inputs",
        type=dict,
        action="append"
    )




    def post(self):

        # get the arguments using parser
        
        data=UserResource.parser.parse_args()        
        print((data["inputs"][0]))

        jsondata=data["inputs"][0]
        print(jsondata["name"])
        

        return  {"message":"users added"}
        user=UserModel(data["name"],data["age"])
        # print(f"user : {json.dumps(user.__dict__)}")
       
        
        user.saveToDb()
        user=user.convert()
        print(f"user to be added is {user}")
        
     
        # return json.dumps(user)
        return {"message":"added"}
    
    def get(self):
        
        data=UserModel.getUsers()
        list=[data.convert() for data in data]        
        return json.dumps(list,sort_keys=True)
    

    # delete
    def delete(self):
        data=UserModel.getUsers()
        for data in data:
            data.deleteFromDb()

        return {"message":"data deleted"}
    
    # @classmethod
    # def convert(cls,data):
    #     data=data.__dict__
    #     print(data)
    #     data.pop("_sa_instance_state")
    #     return data

