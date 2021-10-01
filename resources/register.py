from flask_restful import Resource,reqparse


class RegisterResource(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("username",type=str)
    parser.add_argument("password",type=str)

    def post(self):


        return {"message":"user registered"}

