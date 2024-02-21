from flask import jsonify, request,make_response
from models import Category,db
from flask_restful import Resource

#Creating/Posting category
class Category(Resource):
    def post_category():
        data = request.get_json()
        category = Category(name=data['name'])
        db.session.add(category)
        db.session.commit()
        return make_response(jsonify(['Category Added successfuly']),200)    
    
#Getting all categories
    def get_categories():
        categories=[]
        for category in Category.query.all():
            category_dict={
               "id":category.id,               
                "name":category.name
                          
                }
            categories.append(category_dict)
        return make_response(jsonify(categories),200)
    
    
class CategoryByID(Resource):
    def get_category(id):
        category = Category.query.get(id)
        category_dict={
               "id":category.id,               
                "name":category.name
                          
                }
        return make_response(jsonify(category_dict),200)
    
    #update category
    def update_category(id):
        category = Category.query.get(id)
        data = request.json
        for field in ['id','name']:
            if field in data:
                setattr(category,field,data[field])
        db.session.commit()
        return make_response(jsonify(['Category updated successfully']),200)

    def delete_category(id):
        category = Category.query.filter_by(id=id).first()
        db.session.delete(category)
        db.session.commit()
        return make_response(jsonify(["Deleted successfully"]),200)
