from models import Subscription,db
from flask import jsonify,request, make_response
from flask_restful import Resource

class Subscriptions(Resource):
    def post(self):
        data = request.get_json()
        subscription = Subscription(category_id=data['category_id'],user_id=data['user_id'])
        db.session.add(subscription)
        db.session.commit()
        return make_response(jsonify({"message":"subscription updated successfully"}), 201)
    
    def get(self):
        subscriptions_list=[]
        for subscription in Subscription.query.all():
            subscription_dict={
                "id":subscription.id,               
                    "user_id":subscription.user_id,
                    "category_id":subscription.category_id
                            
                    }
            subscriptions_list.append(subscription_dict)
        return make_response(jsonify(subscriptions_list), 200)
    
class SubscriptionByID(Resource):
    def get(self, id):
        subscription = Subscription.query.filter_by(id=id).first()
        subscription_dict={
                "id":subscription.id,               
                    "user_id":subscription.user_id,
                    "category_id":subscription.category_id
        }
        return make_response(jsonify(subscription_dict), 200)
    
    def put(self, id):
        subscription = Subscription.query.filter_by(id=id).first()
        data = request.json
        for field in ["id","user_id","category_id"]:
            if field in data:
                setattr(subscription,field,data[field])
        db.session.commit()
        return make_response((jsonify({"message":"subscription updated successfully"}), 201
    ))
    def delete(self,id):
        subscription = Subscription.query.filter_by(id=id).first()
        db.session.delete(subscription)
        db.session.commit()
        return make_response(jsonify({"message":"subscription updated successfully"}), 200
)