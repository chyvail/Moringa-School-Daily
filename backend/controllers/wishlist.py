from models import Wishlist,db
from flask import jsonify,request, make_response
from flask_restful import Resource

class Wishlists(Resource):
    def post(self):
        data = request.get_json()
        wishlist = Wishlist(content_id=data['content_id'],user_id=data['user_id'])
        db.session.add(wishlist)
        db.session.commit()
        return make_response(jsonify({"message":"Wishlist added successfully"}), 201)
    
    def get(self):
        wishlist_items=[]
        for wishlist in Wishlist.query.all():
            wishlist_dict={
                "id":wishlist.id,               
                    "user_id":wishlist.user_id,
                    "content_id":wishlist.content_id
            }                          
                    
            wishlist_items.append(wishlist_dict)
        return make_response(jsonify(wishlist_items), 200)
    
class WishlistByID(Resource):
    def get(self, id):
        wishlist = Wishlist.query.filter_by(id=id).first()
        wishlist_dict={
                "id":wishlist.id,               
                    "user_id":wishlist.user_id,
                    "content_id":wishlist.content_id
        }
        return make_response(jsonify(wishlist_dict), 200)
    
    def patch(self, id):
        wishlist = Wishlist.query.filter_by(id=id).first()
        data = request.json
        for field in ["id","user_id","content_id"]:
            if field in data:
                setattr(wishlist,field,data[field])
        db.session.commit()
        return make_response(jsonify({"message":"Wishlist updated successfully"}), 201
    )
    def delete(self,id):
        wishlist = Wishlist.query.filter_by(id=id).first()
        db.session.delete(wishlist)
        db.session.commit()
        return make_response(jsonify({"message":"Wishlist deleted successfully"}), 200)