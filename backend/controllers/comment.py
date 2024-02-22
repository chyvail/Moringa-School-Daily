from models import Comment, db
from flask import jsonify, request, make_response
from flask_restful import Resource

class Comments(Resource):
    def post(self):
        try:
            data = request.get_json()
            comment = Comment(comment=data['comment'], user_id=data['user_id'], content_id=data['content_id'])
            db.session.add(comment)
            db.session.commit()
            return make_response(jsonify(["Comment added successfully"]), 200)
        except KeyError:
            return make_response(jsonify({'error': 'Missing required data in the request.'}), 400)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

    def get(self):
        try:
            comments_list = []
            for comment in Comment.query.all():
                comment_dict = {
                    "id": comment.id,
                    "comment": comment.comment,
                    "user_id": comment.user_id,
                    "content_id": comment.content_id
                }
                comments_list.append(comment_dict)
            return make_response(jsonify(comments_list), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

class CommentByID(Resource):
    def get(self, id):
        try:
            comment = Comment.query.filter_by(id=id).first()
            if comment:
                comment_dict = {
                    "id": comment.id,
                    "comment": comment.comment,
                    "user_id": comment.user_id,
                    "content_id": comment.content_id
                }
                return make_response(jsonify(comment_dict), 200)
            else:
                return make_response(jsonify({'error': 'Comment not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

    def patch(self, id):
        try:
            comment = Comment.query.filter_by(id=id).first()
            if comment:
                data = request.json
                for field in ["comment", "user_id", "content_id"]:
                    if field in data:
                        setattr(comment, field, data[field])
                db.session.commit()
                return make_response(jsonify(["Updated successfully"]), 200)
            else:
                return make_response(jsonify({'error': 'Comment not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        try:
            comment = Comment.query.filter_by(id=id).first()
            if comment:
                db.session.delete(comment)
                db.session.commit()
                return make_response(jsonify(["Deleted successfully"]), 200)
            else:
                return make_response(jsonify({'error': 'Comment not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
