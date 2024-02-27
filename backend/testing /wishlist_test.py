import json
from app import app
from models import db, Wishlist

class TestWishlists:
    def test_wishlists_post_route_creates_wishlist_record_in_db(self):
        '''allows users to create Wishlist records through the "/wishlists" POST route.'''
        response = app.test_client().post(
            '/wishlists',
            json = {
                "user_id": 1,
                "content_id": 1
            }
        )

        assert response.status_code == 201
        assert json.loads(response.data.decode()) == {"message": "wishlist created successfully"}

        with app.app_context():
            wishlist = Wishlist.query.filter_by(user_id=1, content_id=1).first()
            assert wishlist is not None

            db.session.delete(wishlist)
            db.session.commit()

    def test_wishlists_get_route_returns_list_of_wishlists(self):
        '''returns JSON representing Wishlist objects at "/wishlists".'''
        with app.app_context():
            wishlist = Wishlist(user_id=1, content_id=1)
            db.session.add(wishlist)
            db.session.commit()

            response = app.test_client().get('/wishlists')
            data = json.loads(response.data.decode())
            assert type(data) == list
            assert len(data) == 1
            assert data[0]["user_id"] == 1
            assert data[0]["content_id"] == 1

            db.session.delete(wishlist)
            db.session.commit()

    def test_wishlist_by_id_get_route(self):
        '''has a resource available at "/wishlists/<int:id>".'''
        with app.app_context():
            wishlist = Wishlist(user_id=1, content_id=1)
            db.session.add(wishlist)
            db.session.commit()

            response = app.test_client().get('/wishlists/1')
            assert response.status_code == 200

            db.session.delete(wishlist)
            db.session.commit()

    def test_wishlist_by_id_get_route_returns_one_wishlist(self):
        '''returns JSON representing one Wishlist object at "/wishlists/<int:id>".'''
        with app.app_context():
            wishlist = Wishlist(user_id=1, content_id=1)
            db.session.add(wishlist)
            db.session.commit()

            response = app.test_client().get('/wishlists/1')
            data = json.loads(response.data.decode())
            assert data["user_id"] == 1
            assert data["content_id"] == 1

            db.session.delete(wishlist)
            db.session.commit()

    def test_wishlist_patch_route_updates_wishlist_record_in_db(self):
        '''allows users to update Wishlist records through the "/wishlists/<int:id>" PATCH route.'''
        with app.app_context():
            wishlist = Wishlist(user_id=1, content_id=1)
            db.session.add(wishlist)
            db.session.commit()

            response = app.test_client().patch(
                '/wishlists/1',
                json = {
                    "user_id": 2,
                    "content_id": 2
                }
            )

            assert response.status_code == 201
            assert json.loads(response.data.decode()) == {"message": "Wishlist updated successfully"}

            updated_wishlist = Wishlist.query.get(1)
            assert updated_wishlist.user_id == 2
            assert updated_wishlist.content_id == 2

            db.session.delete(updated_wishlist)
            db.session.commit()

    def test_wishlist_delete_route_deletes_wishlist_record_from_db(self):
        '''allows users to delete Wishlist records through the "/wishlists/<int:id>" DELETE route.'''
        with app.app_context():
            wishlist = Wishlist(user_id=1, content_id=1)
            db.session.add(wishlist)
            db.session.commit()

            response = app.test_client().delete('/wishlists/1')

            assert response.status_code == 200
            assert json.loads(response.data.decode()) == {"message": "Wishlist deleted successfully"}

            deleted_wishlist = Wishlist.query.get(1)
            assert deleted_wishlist is None
