from flask_restful import Resource,reqparse


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
        args=UserResource.parser.parse_args()
        
        print(args)
        return args
    
    def get(self):
        args=UserResource.parser.parse_args()
        return args
    
    def delete(self):
        return 
