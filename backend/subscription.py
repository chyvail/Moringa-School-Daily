from models import Subscription,db
from flask import jsonify,request
from flask_restful import Resource

class Subscription(Resource):
    def post(self):
        data = request.get_json()
        subscription = Subscription(category_id=data['category_id'],user_id=data['user_id'])
        db.session.add(subscription)
        db.session.commit()
        return jsonify(["Subscription added successfully"])
