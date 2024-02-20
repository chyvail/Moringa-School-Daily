from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from http import HTTPStatus

app = Flask(__name__)

api = Api(app)

# class Home(Resource):
    
#     def get(self):
#         response_dict = {
#             "Message": "Moringa School Daily API",
#         }
#         response = make_response(
#             response_dict,
#             HTTPStatus.OK,
#         )
#         return response

# api.add_resource(Home, '/')

if __name__=='__main__':
    app.run()