from flask import jsonify, request
from models import Category,db

#Creating/Posting category
def post_category():
    data = request.get_json()
    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()
    return jsonify(['Category Added successfuly'])
    
    
#Getting all categories
def get_categories():
    categories=[]
    for category in Category.query.all():
        category_dict={
               "id":category.id,               
                "name":category.name
                          
                }
        categories.append(category_dict)
    return jsonify(categories)
    
    

def get_category(id):
    category = Category.query.get(id)
    category_dict={
               "id":category.id,               
                "name":category.name
                          
                }
    return jsonify(category_dict)

