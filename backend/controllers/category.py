from flask import jsonify, request, make_response
from models import Category, db
from flask_restful import Resource

class Categories(Resource):
    def post(self):
        try:
            data = request.get_json()
            category = Category(name=data['name'])
            db.session.add(category)
            db.session.commit()
            return make_response(jsonify(['Category Added successfully']), 200) 
        except KeyError:
            return make_response(jsonify({'error': 'Missing required field'}), 400)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)

    def get(self):
        try:
            category_list = []
            for category in Category.query.all():
                category_dict = {
                    "id": category.id,               
                    "name": category.name
                }
                category_list.append(category_dict)
            return make_response(jsonify(category_list), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
class CategoryByID(Resource):
    def get(self, id):
        try:
            category = Category.query.get(id)
            if not category:
                return make_response(jsonify({'error': 'Category not found'}), 404)
            category_dict = {
                "id": category.id,               
                "name": category.name
            }
            return make_response(jsonify(category_dict), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def patch(self, id):
        try:
            category = Category.query.get(id)
            if not category:
                return make_response(jsonify({'error': 'Category not found'}), 404)
            data = request.json
            for field in ['name']:
                if field in data:
                    setattr(category, field, data[field])
            db.session.commit()
            return make_response(jsonify(['Category updated successfully']), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)

    def delete(self, id):
        try:
            category = Category.query.get(id)
            if not category:
                return make_response(jsonify({'error': 'Category not found'}), 404)
            db.session.delete(category)
            db.session.commit()
            return make_response(jsonify(["Deleted successfully"]), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
