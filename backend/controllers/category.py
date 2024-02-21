from flask import jsonify, request
from models import Category,db
from flask_restful import Resource

#Creating/Posting category
class Category(Resource):
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
    
    
class CategoryByID(Resource):
    def get_category(id):
        category = Category.query.get(id)
        category_dict={
               "id":category.id,               
                "name":category.name
                          
                }
        return jsonify(category_dict)
    
    #update category
    def update_category(id):
        category = Category.query.get(id)
        data = request.json
        for field in ['id','name']:
            if field in data:
                setattr(category,field,data[field])
        db.session.commit()
        return jsonify(['Category updated successfully'])

    def delete_category(id):
        category = Category.query.filter_by(id=id).first()
        db.session.delete(category)
        db.session.commit()
        return jsonify(["Deleted successfully"])
