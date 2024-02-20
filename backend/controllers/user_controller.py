from models import User,db
from flask import jsonify,request



#Post user
def post_user():
    data = request.get_json()
    user = User(id = data['id'],firstname = data['firstname'],lastname=data['lastname'], email=data['email'],password = data['password'],role = data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify(["User added successfully"])

#get all users

# def get_users():
#     users=User.query.all()
#     return jsonify([user.to_dict() for user in users])

#get single user
def get_user(id):
    user = User.query.filter_by(id=id).first()
    user_dict={
               "id":user.id, 
               "firstname":user.firstname, 
               "lastname":user.lastname,
                "role":user.role, 
                "email":user.email,
                "comments": [comment.comment for comment in user.comments],
                # "wishlist":[wishlist.content_id for wishlist in user.wishlist]
                }
    return jsonify(user_dict)

def get_users():
    users_list=[]
    for user in User.query.all():
        user_dict={
               "id":user.id, 
               "firstname":user.firstname, 
               "lastname":user.lastname,
                "role":user.role, 
                "email":user.email,
                "comments": [comment.comment for comment in user.comments]
                # "profile": user.profiles.bio
                }
        users_list.append(user_dict)
    return jsonify(users_list)

#update user
def update_user(id):
    user = User.query.get(id)    

    data=request.json
    for field in ['id', 'firstname', 'lastname', 'email', 'password', 'role']:
        if field in data:
            setattr(user, field, data[field])
    db.session.commit()

    return jsonify(["User updated successfully"])

def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(["User deleted successfully"])

    




