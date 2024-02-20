from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from http import HTTPStatus
from controllers.users import Users
from controllers.recommendation import Recommendations, RecommendationByID
from controllers.subscription import Subscriptions, SubscriptionByID
from controllers.wishlist import Wishlists, WishlistByID
from flask_cors import CORS
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moringa-daily.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app,db)

db.init_app(app)

CORS(app)

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
api.add_resource(RecommendationByID, '/recommendations<int:id>')
api.add_resource(Subscriptions, '/subscriptions')
api.add_resource(SubscriptionByID, '/subscriptions/<int:id>')
api.add_resource(Wishlists, '/wishlists')
api.add_resource(WishlistByID, '/wishlists/<int:id>')
api.add_resource(Users,'/users')

if __name__=='__main__':
    app.run()