from models import Comment,db
from flask import jsonify,request,make_response
from flask_restful import Resource

from flask import request, jsonify, make_response
from werkzeug.exceptions import NotFound, BadRequest
from sqlalchemy.exc import SQLAlchemyError

class Comments(Resource):
    def post(self):
        try:
            data = request.get_json()
            if not data or 'comment' not in data or 'user_id' not in data or 'content_id' not in data:
                raise BadRequest("Invalid request data. 'comment', 'user_id', and 'content_id' are required.")

            comment = Comment(comment=data['comment'], user_id=data['user_id'], content_id=data['content_id'])
            db.session.add(comment)
            db.session.commit()

            return make_response(jsonify({"message": "Comment added successfully"}), 200)
        
        except BadRequest as e:
            return make_response(jsonify({"error": str(e)}), 400)
        
        except SQLAlchemyError as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Database error occurred."}), 500)
        
        except Exception as e:
            return make_response(jsonify({"error": "An unexpected error occurred."}), 500)



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
            return make_response(jsonify({"error": "An unexpected error occurred."}), 500)


class CommentByID(Resource):
    def get(self, id):
        try:
            comment = Comment.query.filter_by(id=id).first()
            if comment is None:
                raise NotFound("Comment not found.")
            
            comment_dict = {
                "id": comment.id, 
                "comment": comment.comment, 
                "user_id": comment.user_id,
                "content_id": comment.content_id                
            }
            
            return make_response(jsonify(comment_dict), 200)
        
        except NotFound as e:
            return make_response(jsonify({"error": str(e)}), 404)
        
        except Exception as e:
            return make_response(jsonify({"error": "An unexpected error occurred."}), 500)

    def patch(self, id):
        try:
            comment = Comment.query.filter_by(id=id).first()
            if comment is None:
                raise NotFound("Comment not found.")

            data = request.json
            for field in ["id", "comment", "user_id", "content_id"]:
                if field in data:
                    setattr(comment, field, data[field])
            db.session.commit()

            return make_response(jsonify(["Updated successfully"]), 200)
        
        except NotFound as e:
            return make_response(jsonify({"error": str(e)}), 404)

        except SQLAlchemyError as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Database error occurred."}), 500)
        
        except Exception as e:
            return make_response(jsonify({"error": "An unexpected error occurred."}), 500)

    def delete(self, id):
        try:
            comment = Comment.query.filter_by(id=id).first()
            if comment is None:
                raise NotFound("Comment not found.")
            
            db.session.delete(comment)
            db.session.commit()

            return make_response(jsonify(["Deleted successfully"]), 200)
        
        except NotFound as e:
            return make_response(jsonify({"error": str(e)}), 404)

        except SQLAlchemyError as e:
            db.session.rollback()
            return make_response(jsonify({"error": "Database error occurred."}), 500)
        
        except Exception as e:
            return make_response(jsonify({"error": "An unexpected error occurred."}), 500)




