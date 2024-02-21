from flask import jsonify, request
from models import Profile,db
from flask_restful import Resource


class Profile(Resource):
    def post_profile():
        data = request.get_json()
        profile = Profile(profile_picture = data['profile_picture'],bio = data['bio'],user_id=data['user_id'])
        db.session.add(profile)
        db.session.commit()
        return jsonify(["Profile Added successfully"])
    
    def get_profiles():    
        profiles_list=[]
        for profile in Profile.query.all():
             profile_dict = {
            "id":profile.id,
            "profile_picture":profile.profile_picture,
            "bio":profile.bio,
            "user_id":profile.user_id
        }
        profiles_list.append(profile_dict)
        return jsonify(profiles_list)
    

class ProfileByID(Resource):
    def get_profile(id):
        profile = Profile.query.get(id)
        profile_dict = {
            "id":profile.id,
            "profile_picture":profile.profile_picture,
            "bio":profile.bio,
            "user_id":profile.user_id
        }
        return jsonify(profile_dict)  

    def update_profile(id):
        profile =Profile.query.get(id)
        data = request.json
        for field in ['id','profile_picture','bio','user_id']:
            if field in data:
                setattr(profile,field,data[field])
        db.session.commit()
        return jsonify(["Profile updated successfully"])
    
    def delete_profile(id):
        profile = Profile.query.get(id)
        db.session.delete(profile)
        db.session.commit()
        return jsonify(["Deleted successfully"])