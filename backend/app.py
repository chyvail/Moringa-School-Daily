from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from http import HTTPStatus
from controllers.recommendation import Recommendations, RecommendationByID
from controllers.subscription import Subscription, SubscriptionByID
from controllers.wishlist import Wishlist, WishlistByID

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
api.add_resource(Recommendations, '/recommendations')
api.add_resource(RecommendationByID, '/recommendations<int:id>')
api.add_resource(Subscription, '/subscriptions')
api.add_resource(SubscriptionByID, '/subscriptions/<int:id>')
api.add_resource(Wishlist, '/wishlists')
api.add_resource(WishlistByID, '/wishlists/<int:id>')

if __name__=='__main__':
    app.run()