from models import Wishlist,db
from flask import jsonify,request
from flask_restful import Resource

class Wishlists(Resource):
    def post():
        data = request.get_json()
        wishlist = Wishlist(content_id=data['content_id'],user_id=data['user_id'])
        db.session.add(wishlist)
        db.session.commit()
        return jsonify(["Wishlist added successfully"])
