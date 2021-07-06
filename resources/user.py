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
        print(data)
        for data in data["inputs"]:
            user=UserModel(data["name"],data["age"],data["count"],data["marks"])
            user.saveToDb()
        

        return  {"message":"users added"}
        user=UserModel(data["name"],data["age"])
        # print(f"user : {json.dumps(user.__dict__)}")
       
        
        user.saveToDb()
        user=user.convert()
        print(f"user to be added is {user}")
        
     
        # return json.dumps(user)
        return {"message":"added"}
    
    def get(self):
        # get all users
        users=UserModel.getUsers()     
        # print(f"users is :{users}")
        list=[users.convert() for users in users]
        # print(list)        
        return json.dumps(list,sort_keys=True)

        # get count
        # count=UserModel.getCount()

        # print(f"count is {count}")

        # return {"count":"count"}

        # get total marks
        
        # marks=UserModel.getTotalMarks()
        # print(f"marks {marks[0]}")
        # return {"marks":marks[0]}
    

    # delete
    def delete(self):
        data=UserModel.getUsers()
        for data in data:
            data.deleteFromDb()

        return {"message":"data deleted"}
    

    def put(self):
        data=UserResource.parser.parse_args() 
        
        EID=data["inputs"][0]["id"]
        print(f"id : {EID}")
        user=UserModel.getSingleUser(EID)
        print(f"user to be upadated")
        user.name=data["inputs"][0]["name"]

        user.saveToDb()

        return {"message":"user udpated"}



    # @classmethod
    # def convert(cls,data):
    #     data=data.__dict__
    #     print(data)
    #     data.pop("_sa_instance_state")
    #     return data

