from models import db,Content
from flask import jsonify,request,make_response
from datetime import datetime
from flask_restful import Resource


class Content(Resource):
    def post_content():
        data = request.get_json()
        published_date_str = data.get('published_date', '')
        published_date = datetime.strptime(published_date_str, '%Y-%m-%d').date()
        data['published_date'] = published_date
        content = Content(title=data['title'],description=data['description'],content_type=data['content_type'],published_date = data['published_date'],content_url=data['content_url'],likes=data['likes'],dislikes=data['dislikes'],flagged=data['flagged'],status=data['status'],user_id=data["user_id"],category_id=data['category_id'])
        db.session.add(content)
        db.session.commit()
        return make_response(jsonify(["Added successfully"]),200)
    
    def get_contents():
        content_list=[]
        for content in Content.query.all():
            content_dict={
               "id":content.id, 
               "title":content.title, 
               "description":content.description,
                "content_type":content.content_type,
                "published_date":content.published_date, 
                "content_url":content.content_url ,
                "likes":content.likes,
                "dislikes":content.dislikes,
                "flagged":content.flagged,
                "status":content.status,
                "user_id":content.user_id,
                "category_id":content.category_id,
                "comments":[comment.comment for comment in content.comments]
                          
            }
            content_list.append(content_dict)
        return make_response(jsonify(content_list),200)
    
class ContentByID(Resource):
    def get_content(id):
        content =  Content.query.filter_by(id=id).first()
        content_dict={
               "id":content.id, 
               "title":content.title, 
               "description":content.description,
                "content_type":content.content_type,
                "published_date":content.published_date, 
                "content_url":content.content_url ,
                "likes":content.likes,
                "dislikes":content.dislikes,
                "flagged":content.flagged,
                "status":content.status,
                "user_id":content.user_id,
                "category_id":content.category_id
                          
            }
        return make_response(jsonify(content_dict),200)
    
    def update_content(id):
        content = Content.query.filter_by(id=id).first()
        data = request.get_json()
        for field in ['id','title','description','content_type','published_date','content_url','likes','dislikes','flagged','status']:
            if field in data:
                setattr(content,field,data[field])
        db.session.commit()
        return make_response(jsonify('Content updated successfully'),200)
    
    def delete_content(id):
        content = Content.query.get(id)
        db.session.delete(content)
        db.session.commit()
        return make_response(jsonify(['Deleted successfully']),200)



