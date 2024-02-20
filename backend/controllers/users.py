from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource, abort
from flask_bcrypt import Bcrypt
from models import User,db
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

bcrypt = Bcrypt()
jwt = JWTManager()

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
    
class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            abort(404, detail="User does not exist")
        if not bcrypt.check_password_hash(user.password, data['password']):
            abort(403, detail="Password is not correct")
        metadata = {"role": user.role}
        token = create_access_token(identity=user.email, additional_claims=metadata)
        return {"jwt-access-token": token}

class UserById(Resource):
    def get(self,id):
        user = User.query.get(id)
        if not user:
            abort(404, detail = f'User with {id=} does not exist')
        return user.to_dict()
    
    def patch(self,id):
        user = User.query.get(id)
        if not user:
            abort(404, detail = f'User with {id=} does not exist')
        data = request.get_json()
        for key, value in data.items():
            if value is None:
                continue
            setattr(user, key, value)
        db.session.commit()
        return user.to_dict()
    
    def delete(self,id):
        user = User.query.filter_by(id=id).first()
        if not user:
            abort(404, detail = f'User with {id=} does not exist')
        db.session.delete(user)
        db.session.commit()
        return {"detail": f"user with {id=} has been deleted successfully"}