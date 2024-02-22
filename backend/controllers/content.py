from models import db, Content, Category
from flask import jsonify, request, make_response
from datetime import datetime
from flask_restful import Resource


class Contents(Resource):
    def post(self):
        try:
            data = request.get_json()
            content = Content(
                title=data['title'],
                description=data['description'],
                content_type=data['content_type'],
                image_url=data['image_url'],
                user_id=data['user_id'],
                category_id=data['category_id']
            )
            db.session.add(content)
            db.session.commit()
            return make_response(jsonify(content.to_dict()), 201)
        except KeyError as e:
            return make_response(jsonify({'error': 'Missing required field: {}'.format(str(e))}), 400)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def get(self):
        try:
            content_list = []
            for content in Content.query.all():
                content_dict = {
                    "id": content.id,
                    "title": content.title,
                    "description": content.description,
                    "content_type": content.content_type,
                    "published_date": content.published_date.strftime('%Y-%m-%d %H:%M:%S') if content.published_date else None,
                    "image_url": content.image_url,
                    "likes": content.likes,
                    "dislikes": content.dislikes,
                    "flagged": content.flagged,
                    "public_status": content.public_status,
                    "user_id": content.user_id,
                    "category_id": content.category_id,
                    "comments": [comment.comment for comment in content.comments]
                }
                content_list.append(content_dict)
            return make_response(jsonify(content_list), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

class ContentByID(Resource):
    def get(self, id):
        try:
            content = Content.query.filter_by(id=id).first()
            if content:
                content_dict = {
                    "id": content.id,
                    "title": content.title,
                    "description": content.description,
                    "content_type": content.content_type,
                    "published_date": content.published_date.strftime('%Y-%m-%d %H:%M:%S') if content.published_date else None,
                    "image_url": content.image_url,
                    "likes": content.likes,
                    "dislikes": content.dislikes,
                    "flagged": content.flagged,
                    "public_status": content.public_status,
                    "user_id": content.user_id,
                    "category_id": content.category_id,
                }
                return make_response(jsonify(content_dict), 200)
            else:
                return make_response(jsonify({'error': 'Content not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def patch(self, id):
        try:
            content = Content.query.filter_by(id=id).first()
            if content:
                data = request.get_json()
                for field in ['title', 'description', 'content_type', 'published_date', 'image_url', 'likes', 'dislikes', 'flagged', 'public_status']:
                    if field in data:
                        setattr(content, field, data[field])
                db.session.commit()
                return make_response(jsonify('Content updated successfully'), 200)
            else:
                return make_response(jsonify({'error': 'Content not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        try:
            content = Content.query.get(id)
            if content:
                db.session.delete(content)
                db.session.commit()
                return make_response(jsonify(['Deleted successfully']), 200)
            else:
                return make_response(jsonify({'error': 'Content not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
