from models import Comment,db
from flask import jsonify,request
from flask_restful import Resource

class Comment(Resource):
    def post_comment():
        data = request.get_json()
        comment = Comment(comment=data['comment'],user_id=data['user_id'],content_id=data['content_id'])
        db.session.add(comment)
        db.session.commit()
        return jsonify(["Comment added successfully"])


    def get_comments():
        comments_list=[]
        for comment in Comment.query.all():
            comment_dict={
               "id":comment.id, 
               "comment":comment.comment, 
               "user_id":comment.user_id,
                "content_id":comment.content_id                
                }
            comments_list.append(comment_dict)
            return jsonify(comments_list)

class CommentByID(Resource):

    def get_comment(id):
        comment = Comment.query.filter_by(id=id).first()
        comment_dict={
               "id":comment.id, 
               "comment":comment.comment, 
               "user_id":comment.user_id,
                "content_id":comment.content_id                
                }
        return jsonify(comment_dict)

    def update_comment(id):
        comment = Comment.query.filter_by(id=id).first()
        data = request.json
        for field in ["id","comment","user_id","content_id"]:
            if field in data:
                 setattr(comment,field,data[field])
        db.session.commit()
        return jsonify(["Updated successfully"])
    
    def delete_comment(id):
        comment = Comment.query.filter_by(id=id).first()
        db.session.delete(comment)
        db.session.commit()
        return jsonify(["Deleted successfully"])




