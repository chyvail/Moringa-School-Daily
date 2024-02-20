from models import Wishlist,db
from flask import jsonify,request
from flask_restful import Resource

class Wishlists(Resource):
    def post(self):
        data = request.get_json()
        wishlist = Wishlist(content_id=data['content_id'],user_id=data['user_id'])
        db.session.add(wishlist)
        db.session.commit()
        return jsonify(["Wishlist added successfully"])
    
    def get(self):
        wishlist_items=[]
        for wishlist in Wishlist.query.all():
            wishlist_dict={
                "id":wishlist.id,               
                    "user_id":wishlist.user_id,
                    "content_id":wishlist.content_id
            }                          
                    
            wishlist_items.append(wishlist_dict)
        return jsonify(wishlist_items)
class WishlistByID(Resource):
    def get(self, id):
        wishlist = Wishlist.query.filter_by(id=id).first()
        wishlist_dict={
                "id":wishlist.id,               
                    "user_id":wishlist.user_id,
                    "content_id":wishlist.content_id
        }
        return jsonify(wishlist_dict)
    def update(self, id):
        wishlist = Wishlist.query.filter_by(id=id).first()
        data = request.json
        for field in ["id","user_id","content_id"]:
            if field in data:
                setattr(wishlist,field,data[field])
        db.session.commit()
        return jsonify(["Updated successfully"])