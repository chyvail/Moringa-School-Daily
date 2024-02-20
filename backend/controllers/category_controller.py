from flask import jsonify, request
from models import Category,db

#Creating/Posting category
def post_category():
    data = request.get_json()
    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()
    return jsonify(['Category Added successfuly'])
    
    


