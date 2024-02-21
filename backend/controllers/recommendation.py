from models import Recommendation,db
from flask import jsonify,request, make_response
from flask_restful import Resource

class Recommendations(Resource):
    def post(self):
        data=request.get_json()
        recommendation=Recommendation(content_id=data['content_id'],user_id=data['user_id'])
        db.session.add(recommendation)
        db.session.commit()
        return jsonify({"message":"recommendation added successfully"}), 201

    def get(self):
        recommendations_list=[]
        for recommendation in Recommendation.query.all():
            recommendation_dict={
                "id": recommendation.id,
                "user_id":recommendation.user_id,
                "content_id": recommendation.content_id
            }
            recommendations_list.append(recommendation_dict)
        return make_response(jsonify(recommendations_list), 200)
    
class RecommendationByID(Resource):
    def get(self, id):
        recommendation= Recommendation.query.filter_by(id=id).first()
        recommendation_dict={
                "id": recommendation.id,
                "user_id":recommendation.user_id,
                "content_id": recommendation.content_id
            }
        return make_response(jsonify(recommendation_dict), 200)

    def patch(self, id):
        recommendation = Recommendation.query.filter_by(id=id).first()
        data = request.json
        for field in ["id","user_id","content_id"]:
            if field in data:
                setattr(recommendation,field,data[field])
        db.session.commit()
        return make_response(jsonify({"message":"recommendation updated successfully"}), 201)

    def delete(id):
        recommendation = Recommendation.query.filter_by(id=id).first()
        db.session.delete(recommendation)
        db.session.commit()
        return make_response(jsonify({"message":"recommendation deleted successfully"}), 200)