import json
from app import app
from models import db, Recommendation

class TestRecommendations:
    def test_recommendations_post_route_creates_recommendation_record_in_db(self):
        '''allows users to create Recommendation records through the "/recommendations" POST route.'''
        response = app.test_client().post(
            '/recommendations',
            json = {
                "user_id": 1,
                "content_id": 1
            }
        )

        assert response.status_code == 201
        assert json.loads(response.data.decode()) == {"message": "recommendation created successfully"}

        with app.app_context():
            recommendation = Recommendation.query.filter_by(user_id=1, content_id=1).first()
            assert recommendation is not None

            db.session.delete(recommendation)
            db.session.commit()

    def test_recommendations_get_route_returns_list_of_recommendations(self):
        '''returns JSON representing Recommendation objects at "/recommendations".'''
        with app.app_context():
            recommendation = Recommendation(user_id=1, content_id=1)
            db.session.add(recommendation)
            db.session.commit()

            response = app.test_client().get('/recommendations')
            data = json.loads(response.data.decode())
            assert type(data) == list
            assert len(data) == 1
            assert data[0]["user_id"] == 1
            assert data[0]["content_id"] == 1

            db.session.delete(recommendation)
            db.session.commit()

    def test_recommendation_by_id_get_route(self):
        '''has a resource available at "/recommendations/<int:id>".'''
        with app.app_context():
            recommendation = Recommendation(user_id=1, content_id=1)
            db.session.add(recommendation)
            db.session.commit()

            response = app.test_client().get('/recommendations/1')
            assert response.status_code == 200

            db.session.delete(recommendation)
            db.session.commit()

    def test_recommendation_by_id_get_route_returns_one_recommendation(self):
        '''returns JSON representing one Recommendation object at "/recommendations/<int:id>".'''
        with app.app_context():
            recommendation = Recommendation(user_id=1, content_id=1)
            db.session.add(recommendation)
            db.session.commit()

            response = app.test_client().get('/recommendations/1')
            data = json.loads(response.data.decode())
            assert data["user_id"] == 1
            assert data["content_id"] == 1

            db.session.delete(recommendation)
            db.session.commit()

    def test_recommendation_patch_route_updates_recommendation_record_in_db(self):
        '''allows users to update Recommendation records through the "/recommendations/<int:id>" PATCH route.'''
        with app.app_context():
            recommendation = Recommendation(user_id=1, content_id=1)
            db.session.add(recommendation)
            db.session.commit()

            response = app.test_client().patch(
                '/recommendations/1',
                json = {
                    "user_id": 2,
                    "content_id": 2
                }
            )

            assert response.status_code == 201
            assert json.loads(response.data.decode()) == {"message": "recommendation updated successfully"}

            updated_recommendation = Recommendation.query.get(1)
            assert updated_recommendation.user_id == 2
            assert updated_recommendation.content_id == 2

            db.session.delete(updated_recommendation)
            db.session.commit()

    def test_recommendation_delete_route_deletes_recommendation_record_from_db(self):
        '''allows users to delete Recommendation records through the "/recommendations/<int:id>" DELETE route.'''
        with app.app_context():
            recommendation = Recommendation(user_id=1, content_id=1)
            db.session.add(recommendation)
            db.session.commit()

            response = app.test_client().delete('/recommendations/1')

            assert response.status_code == 200
            assert json.loads(response.data.decode()) == {"message": "recommendation deleted successfully"}

            deleted_recommendation = Recommendation.query.get(1)
            assert deleted_recommendation is None
