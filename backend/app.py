from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from http import HTTPStatus
from controllers.recommendation import Recommendation, RecommendationByID

app = Flask(__name__)

api = Api(app)

class Home(Resource):
    
    def get(self):
        response_dict = {
            "Message": "Moringa School Daily API",
        }
        response = make_response(
            response_dict,
            HTTPStatus.OK,
        )
        return response

api.add_resource(Home, '/')
api.add_resource(Recommendation, '/recommendations')
api.add_resource(RecommendationByID, '/recommendations<int:id>')

if __name__=='__main__':
    app.run()