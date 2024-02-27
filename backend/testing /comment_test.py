import json
from app import app
from models import db, Comment

class TestComments:
    def test_comments_post_route_creates_comment_record_in_db(self):
        '''allows users to create Comment records through the "/comments" POST route.'''
        response = app.test_client().post(
            '/comments',
            json = {
                "comment": "Test Comment",
                "user_id": 1,
                "content_id": 1
            }
        )

        with app.app_context():
            comment = Comment.query.filter_by(comment="Test Comment").first()
            assert(comment.id)
            assert(comment.comment == "Test Comment")
            assert(comment.user_id == 1)
            assert(comment.content_id == 1)

            db.session.delete(comment)
            db.session.commit()

    def test_comments_get_route_returns_list_of_comments(self):
        '''returns JSON representing Comment objects at "/comments".'''
        with app.app_context():
            comment = Comment(comment="Test Comment", user_id=1, content_id=1)
            db.session.add(comment)
            db.session.commit()

            response = app.test_client().get('/comments')
            data = json.loads(response.data.decode())
            assert(type(data) == list)
            for record in data:
                assert(type(record) == dict)
                assert(record['id'])
                assert(record['comment'])
                assert(record['user_id'])
                assert(record['content_id'])

            db.session.delete(comment)
            db.session.commit()

    def test_comment_by_id_get_route(self):
        '''has a resource available at "/comments/<int:id>".'''
        with app.app_context():
            comment = Comment(comment="Test Comment", user_id=1, content_id=1)
            db.session.add(comment)
            db.session.commit()

            response = app.test_client().get('/comments/1')
            assert(response.status_code == 200)

            db.session.delete(comment)
            db.session.commit()

    def test_comment_by_id_get_route_returns_one_comment(self):
        '''returns JSON representing one Comment object at "/comments/<int:id>".'''
        with app.app_context():
            comment = Comment(comment="Test Comment", user_id=1, content_id=1)
            db.session.add(comment)
            db.session.commit()

            response = app.test_client().get('/comments/1')
            data = json.loads(response.data.decode())
            assert(type(data) == dict)
            assert(data["id"])
            assert(data["comment"])
            assert(data["user_id"])
            assert(data["content_id"])

            db.session.delete(comment)
            db.session.commit()

    def test_comment_patch_route_updates_comment_record_in_db(self):
        '''allows users to update Comment records through the "/comments/<int:id>" PATCH route.'''
        with app.app_context():
            comment = Comment(comment="Test Comment", user_id=1, content_id=1)
            db.session.add(comment)
            db.session.commit()

            response = app.test_client().patch(
                '/comments/1',
                json = {
                    "comment": "Updated Test Comment"
                }
            )

            updated_comment = Comment.query.get(1)
            assert(updated_comment.comment == "Updated Test Comment")

            db.session.delete(updated_comment)
            db.session.commit()

    def test_comment_delete_route_deletes_comment_record_from_db(self):
        '''allows users to delete Comment records through the "/comments/<int:id>" DELETE route.'''
        with app.app_context():
            comment = Comment(comment="Test Comment", user_id=1, content_id=1)
            db.session.add(comment)
            db.session.commit()

            response = app.test_client().delete('/comments/1')

            deleted_comment = Comment.query.get(1)
            assert(deleted_comment is None)
