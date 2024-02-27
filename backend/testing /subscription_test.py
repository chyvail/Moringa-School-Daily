import json
from app import app
from models import db, Subscription

class TestSubscriptions:
    def test_subscriptions_post_route_creates_subscription_record_in_db(self):
        '''allows users to create Subscription records through the "/subscriptions" POST route.'''
        response = app.test_client().post(
            '/subscriptions',
            json = {
                "category_id": 1,
                "user_id": 1
            }
        )

        assert response.status_code == 201
        assert json.loads(response.data.decode()) == {"message": "Subscription created successfully"}

        with app.app_context():
            subscription = Subscription.query.filter_by(user_id=1, category_id=1).first()
            assert subscription is not None

            db.session.delete(subscription)
            db.session.commit()

    def test_subscriptions_get_route_returns_list_of_subscriptions(self):
        '''returns JSON representing Subscription objects at "/subscriptions".'''
        with app.app_context():
            subscription = Subscription(user_id=1, category_id=1)
            db.session.add(subscription)
            db.session.commit()

            response = app.test_client().get('/subscriptions')
            data = json.loads(response.data.decode())
            assert type(data) == list
            assert len(data) == 1
            assert data[0]["user_id"] == 1
            assert data[0]["category_id"] == 1

            db.session.delete(subscription)
            db.session.commit()

    def test_subscription_by_id_get_route(self):
        '''has a resource available at "/subscriptions/<int:id>".'''
        with app.app_context():
            subscription = Subscription(user_id=1, category_id=1)
            db.session.add(subscription)
            db.session.commit()

            response = app.test_client().get('/subscriptions/1')
            assert response.status_code == 200

            db.session.delete(subscription)
            db.session.commit()

    def test_subscription_by_id_get_route_returns_one_subscription(self):
        '''returns JSON representing one Subscription object at "/subscriptions/<int:id>".'''
        with app.app_context():
            subscription = Subscription(user_id=1, category_id=1)
            db.session.add(subscription)
            db.session.commit()

            response = app.test_client().get('/subscriptions/1')
            data = json.loads(response.data.decode())
            assert data["user_id"] == 1
            assert data["category_id"] == 1

            db.session.delete(subscription)
            db.session.commit()

    def test_subscription_patch_route_updates_subscription_record_in_db(self):
        '''allows users to update Subscription records through the "/subscriptions/<int:id>" PATCH route.'''
        with app.app_context():
            subscription = Subscription(user_id=1, category_id=1)
            db.session.add(subscription)
            db.session.commit()

            response = app.test_client().patch(
                '/subscriptions/1',
                json = {
                    "user_id": 2,
                    "category_id": 2
                }
            )

            assert response.status_code == 201
            assert json.loads(response.data.decode()) == {"message": "subscription updated successfully"}

            updated_subscription = Subscription.query.get(1)
            assert updated_subscription.user_id == 2
            assert updated_subscription.category_id == 2

            db.session.delete(updated_subscription)
            db.session.commit()

    def test_subscription_delete_route_deletes_subscription_record_from_db(self):
        '''allows users to delete Subscription records through the "/subscriptions/<int:id>" DELETE route.'''
        with app.app_context():
            subscription = Subscription(user_id=1, category_id=1)
            db.session.add(subscription)
            db.session.commit()

            response = app.test_client().delete('/subscriptions/1')

            assert response.status_code == 200
            assert json.loads(response.data.decode()) == {"message": "subscription deleted successfully"}

            deleted_subscription = Subscription.query.get(1)
            assert deleted_subscription is None
