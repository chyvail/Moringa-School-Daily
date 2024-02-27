import json
from app import app
from models import db, Category

class TestCategories:
    def test_categories_post_route_creates_category_record_in_db(self):
        '''allows users to create Category records through the "/categories" POST route.'''
        response = app.test_client().post(
            '/categories',
            json = {
                "name": "Test Category",
                "user_id": 1
            }
        )

        with app.app_context():
            category = Category.query.filter_by(name="Test Category").first()
            assert(category.id)
            assert(category.name == "Test Category")
            assert(category.user_id == 1)

            db.session.delete(category)
            db.session.commit()

    def test_categories_get_route_returns_list_of_categories(self):
        '''returns JSON representing Category objects at "/categories".'''
        with app.app_context():
            category = Category(name="Test Category", user_id=1)
            db.session.add(category)
            db.session.commit()

            response = app.test_client().get('/categories')
            data = json.loads(response.data.decode())
            assert(type(data) == list)
            for record in data:
                assert(type(record) == dict)
                assert(record['id'])
                assert(record['name'])

            db.session.delete(category)
            db.session.commit()

    def test_category_by_id_get_route(self):
        '''has a resource available at "/categories/<int:id>".'''
        with app.app_context():
            category = Category(name="Test Category", user_id=1)
            db.session.add(category)
            db.session.commit()

            response = app.test_client().get('/categories/1')
            assert(response.status_code == 200)

            db.session.delete(category)
            db.session.commit()

    def test_category_by_id_get_route_returns_one_category(self):
        '''returns JSON representing one Category object at "/categories/<int:id>".'''
        with app.app_context():
            category = Category(name="Test Category", user_id=1)
            db.session.add(category)
            db.session.commit()

            response = app.test_client().get('/categories/1')
            data = json.loads(response.data.decode())
            assert(type(data) == dict)
            assert(data["id"])
            assert(data["name"])

            db.session.delete(category)
            db.session.commit()

    def test_category_patch_route_updates_category_record_in_db(self):
        '''allows users to update Category records through the "/categories/<int:id>" PATCH route.'''
        with app.app_context():
            category = Category(name="Test Category", user_id=1)
            db.session.add(category)
            db.session.commit()

            response = app.test_client().patch(
                '/categories/1',
                json = {
                    "name": "Updated Test Category"
                }
            )

            updated_category = Category.query.get(1)
            assert(updated_category.name == "Updated Test Category")

            db.session.delete(updated_category)
            db.session.commit()

    def test_category_delete_route_deletes_category_record_from_db(self):
        '''allows users to delete Category records through the "/categories/<int:id>" DELETE route.'''
        with app.app_context():
            category = Category(name="Test Category", user_id=1)
            db.session.add(category)
            db.session.commit()

            response = app.test_client().delete('/categories/1')

            deleted_category = Category.query.get(1)
            assert(deleted_category is None)

