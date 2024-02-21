from flask import jsonify, request, make_response
from models import Profile, db
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

class Profiles(Resource):
    def post(self):
        try:
            data = request.get_json()
            profile = Profile(profile_picture=data['profile_picture'], bio=data['bio'], user_id=data['user_id'])
            db.session.add(profile)
            db.session.commit()
            return make_response(jsonify(["Profile added successfully"]), 200)
        except KeyError:
            return make_response(jsonify({"error": "Missing required fields"}), 400)
        except SQLAlchemyError as e:
            db.session.rollback()
            return make_response(jsonify({"error": str(e)}), 500)

    def get(self):
        try:
            profiles_list = []
            for profile in Profile.query.all():
                profile_dict = {
                    "id": profile.id,
                    "profile_picture": profile.profile_picture,
                    "bio": profile.bio,
                    "user_id": profile.user_id
                }
                profiles_list.append(profile_dict)
            return make_response(jsonify(profiles_list), 200)
        except SQLAlchemyError as e:
            return make_response(jsonify({"error": str(e)}), 500)

class ProfileByID(Resource):
    def get(self, id):
        try:
            profile = Profile.query.get(id)
            if not profile:
                return make_response(jsonify({"error": "Profile not found"}), 404)
            profile_dict = {
                "id": profile.id,
                "profile_picture": profile.profile_picture,
                "bio": profile.bio,
                "user_id": profile.user_id
            }
            return make_response(jsonify(profile_dict), 200)
        except SQLAlchemyError as e:
            return make_response(jsonify({"error": str(e)}), 500)

    def patch(self, id):
        try:
            profile = Profile.query.get(id)
            if not profile:
                return make_response(jsonify({"error": "Profile not found"}), 404)
            data = request.json
            for field in ['profile_picture', 'bio', 'user_id']:
                if field in data:
                    setattr(profile, field, data[field])
            db.session.commit()
            return make_response(jsonify(["Profile updated successfully"]), 200)
        except SQLAlchemyError as e:
            db.session.rollback()
            return make_response(jsonify({"error": str(e)}), 500)

    def delete(self, id):
        try:
            profile = Profile.query.get(id)
            if not profile:
                return make_response(jsonify({"error": "Profile not found"}), 404)
            db.session.delete(profile)
            db.session.commit()
            return make_response(jsonify(["Profile deleted successfully"]), 200)
        except SQLAlchemyError as e:
            db.session.rollback()
            return make_response(jsonify({"error": str(e)}), 500)
