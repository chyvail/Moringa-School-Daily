import json
from app import app
from models import db, Profile

class TestProfiles:
    def test_profiles_post_route_creates_profile_record_in_db(self):
        '''allows users to create Profile records through the "/profiles" POST route.'''
        response = app.test_client().post(
            '/profiles',
            json = {
                "profile_picture": "test.jpg",
                "bio": "Test Bio",
                "user_id": 1
            }
        )

        with app.app_context():
            profile = Profile.query.filter_by(bio="Test Bio").first()
            assert(profile.id)
            assert(profile.profile_picture == "test.jpg")
            assert(profile.bio == "Test Bio")
            assert(profile.user_id == 1)

            db.session.delete(profile)
            db.session.commit()

    def test_profiles_get_route_returns_list_of_profiles(self):
        '''returns JSON representing Profile objects at "/profiles".'''
        with app.app_context():
            profile = Profile(profile_picture="test.jpg", bio="Test Bio", user_id=1)
            db.session.add(profile)
            db.session.commit()

            response = app.test_client().get('/profiles')
            data = json.loads(response.data.decode())
            assert(type(data) == list)
            for record in data:
                assert(type(record) == dict)
                assert(record['id'])
                assert(record['profile_picture'])
                assert(record['bio'])
                assert(record['user_id'])

            db.session.delete(profile)
            db.session.commit()

    def test_profile_by_id_get_route(self):
        '''has a resource available at "/profiles/<int:id>".'''
        with app.app_context():
            profile = Profile(profile_picture="test.jpg", bio="Test Bio", user_id=1)
            db.session.add(profile)
            db.session.commit()

            response = app.test_client().get('/profiles/1')
            assert(response.status_code == 200)

            db.session.delete(profile)
            db.session.commit()

    def test_profile_by_id_get_route_returns_one_profile(self):
        '''returns JSON representing one Profile object at "/profiles/<int:id>".'''
        with app.app_context():
            profile = Profile(profile_picture="test.jpg", bio="Test Bio", user_id=1)
            db.session.add(profile)
            db.session.commit()

            response = app.test_client().get('/profiles/1')
            data = json.loads(response.data.decode())
            assert(type(data) == dict)
            assert(data["id"])
            assert(data["profile_picture"])
            assert(data["bio"])
            assert(data["user_id"])

            db.session.delete(profile)
            db.session.commit()

    def test_profile_patch_route_updates_profile_record_in_db(self):
        '''allows users to update Profile records through the "/profiles/<int:id>" PATCH route.'''
        with app.app_context():
            profile = Profile(profile_picture="test.jpg", bio="Test Bio", user_id=1)
            db.session.add(profile)
            db.session.commit()

            response = app.test_client().patch(
                '/profiles/1',
                json = {
                    "bio": "Updated Test Bio"
                }
            )

            updated_profile = Profile.query.get(1)
            assert(updated_profile.bio == "Updated Test Bio")

            db.session.delete(updated_profile)
            db.session.commit()

    def test_profile_delete_route_deletes_profile_record_from_db(self):
        '''allows users to delete Profile records through the "/profiles/<int:id>" DELETE route.'''
        with app.app_context():
            profile = Profile(profile_picture="test.jpg", bio="Test Bio", user_id=1)
            db.session.add(profile)
            db.session.commit()

            response = app.test_client().delete('/profiles/1')

            deleted_profile = Profile.query.get(1)
            assert(deleted_profile is None)
