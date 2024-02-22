from flask import jsonify, request, make_response
from models import Profile, db
from flask_restful import Resource

class Profiles(Resource):
    def post(self):
        try:
            data = request.get_json()
            profile = Profile(profile_picture=data['profile_picture'], bio=data['bio'], user_id=data['user_id'])
            db.session.add(profile)
            db.session.commit()
            return make_response(jsonify(["Profile Added successfully"]), 200)
        except KeyError as e:
            return make_response(jsonify({'error': 'Missing required field: {}'.format(str(e))}), 400)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
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
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)

class ProfileByID(Resource):
    def get(self, id):
        try:
            profile = Profile.query.get(id)
            if profile:
                profile_dict = {
                    "id": profile.id,
                    "profile_picture": profile.profile_picture,
                    "bio": profile.bio,
                    "user_id": profile.user_id
                }
                return make_response(jsonify(profile_dict), 200)
            else:
                return make_response(jsonify({'error': 'Profile not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500) 

    def patch(self, id):
        try:
            profile = Profile.query.get(id)
            if profile:
                data = request.json
                for field in ['profile_picture', 'bio', 'user_id']:
                    if field in data:
                        setattr(profile, field, data[field])
                db.session.commit()
                return make_response(jsonify(["Profile updated successfully"]), 200)
            else:
                return make_response(jsonify({'error': 'Profile not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        try:
            profile = Profile.query.get(id)
            if profile:
                db.session.delete(profile)
                db.session.commit()
                return make_response(jsonify(["Deleted successfully"]), 200)
            else:
                return make_response(jsonify({'error': 'Profile not found.'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
