from flask import jsonify, request, make_response
from models import Category, db
from flask_restful import Resource

# Creating/Posting category
class Categories(Resource):
    def post(self):
        try:
            data = request.get_json()
            category = Category(name=data['name'], user_id=data['user_id'])
            db.session.add(category)
            db.session.commit()
            return make_response(jsonify(['Category Added successfully']), 200)
        except KeyError:
            return make_response(jsonify({'error': 'Missing required data in the request.'}), 400)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

    # Getting all categories
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
            if category:
                category_dict = {
                    "id": category.id,
                    "name": category.name
                }
                return make_response(jsonify(category_dict), 200)
            else:
                return make_response(jsonify({'error': 'Category not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

    # Update category
    def patch(self, id):
        try:
            category = Category.query.get(id)
            if category:
                data = request.json
                for field in ['name']:
                    if field in data:
                        setattr(category, field, data[field])
                db.session.commit()
                return make_response(jsonify(['Category updated successfully']), 200)
            else:
                return make_response(jsonify({'error': 'Category not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

    def delete(self, id):
        try:
            category = Category.query.filter_by(id=id).first()
            if category:
                db.session.delete(category)
                db.session.commit()
                return make_response(jsonify(["Deleted successfully"]), 200)
            else:
                return make_response(jsonify({'error': 'Category not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
