from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource, abort
from flask_bcrypt import Bcrypt
from models import User,db

bcrypt = Bcrypt()

class Users(Resource):
    def get(self):
        users_dict = [users.to_dict() for users in User.query.all()]
        return make_response(jsonify(users_dict), 200)
    
    def post(self):
        data = request.get_json()
        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            abort(409, detail="User Already Exists")
        if data['password'] == data['confirm-password']:
            hashed_password = bcrypt.generate_password_hash(data['password'])
            new_user = User(firstname=data['firstname'], lastname=data['lastname'], email=data['email'], password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return make_response(jsonify(new_user.to_dict()),201)
        else:
            abort(403, detail="Password and Confirm Password do not match")
    
