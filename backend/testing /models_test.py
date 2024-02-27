# # tests/test_models.py
# from app import app, db
# from models import User, Content, Category, Profile, Comment, Wishlist, Subscription, Recommendation
# from datetime import datetime

# class TestUser:
#     '''User model in models.py'''

#     def test_can_instantiate(self):
#         '''can be instantiated with a name.'''
#         u = User(firstname="John", lastname="Doe", email="john.doe@example.com", password="password123")
#         assert u
    
#     def test_can_be_created(self):
#         '''can create records that can be committed to the database.'''
#         with app.app_context():
#             u = User(firstname="John", lastname="Doe", email="john.doe@example.com", password="password123")
#             db.session.add(u)
#             db.session.commit()
#             assert u.id

#             db.session.delete(u)
#             db.session.commit()

#     def test_can_be_retrieved(self):
#         '''can be used to retrieve records from the database.'''
#         with app.app_context():
#             u = User.query.all()
#             assert u

#     def test_can_be_serialized(self):
#         '''can create records with a to_dict() method for serialization.'''
#         with app.app_context():
#             u = User(firstname="John", lastname="Doe", email="john.doe@example.com", password="password123")
#             db.session.add(u)
#             db.session.commit()
#             u_dict = u.to_dict()
#             assert isinstance(u_dict, dict) and u_dict["email"] == "john.doe@example.com"
        
#             db.session.delete(u)
#             db.session.commit()

# class TestContent:
#     '''Content model in models.py'''

#     def test_can_instantiate(self):
#         '''can be instantiated with a name.'''
#         c = Content(title="Test Content", description="This is a test content", content_type="Article")
#         assert c
    
#     def test_can_be_created(self):
#         '''can create records that can be committed to the database.'''
#         with app.app_context():
#             c = Content(title="Test Content", description="This is a test content", content_type="Article")
#             db.session.add(c)
#             db.session.commit()
#             assert c.id

#             db.session.delete(c)
#             db.session.commit()

#     def test_can_be_retrieved(self):
#         '''can be used to retrieve records from the database.'''
#         with app.app_context():
#             c = Content.query.all()
#             assert c

#     def test_can_be_serialized(self):
#         '''can create records with a to_dict() method for serialization.'''
#         with app.app_context():
#             c = Content(title="Test Content", description="This is a test content", content_type="Article")
#             db.session.add(c)
#             db.session.commit()
#             c_dict = c.to_dict()
#             assert isinstance(c_dict, dict) and c_dict["title"] == "Test Content"
        
#             db.session.delete(c)
#             db.session.commit()

# class TestCategory:
#     '''Category model in models.py'''

#     def test_can_instantiate(self):
#         '''can be instantiated with a name.'''
#         cat = Category(name="Test Category")
#         assert cat
    
#     def test_can_be_created(self):
#         '''can create records that can be committed to the database.'''
#         with app.app_context():
#             cat = Category(name="Test Category")
#             db.session.add(cat)
#             db.session.commit()
#             assert cat.id

#             db.session.delete(cat)
#             db.session.commit()

#     def test_can_be_retrieved(self):
#         '''can be used to retrieve records from the database.'''
#         with app.app_context():
#             cat = Category.query.all()
#             assert cat

#     def test_can_be_serialized(self):
#         '''can create records with a to_dict() method for serialization.'''
#         with app.app_context():
#             cat = Category(name="Test Category")
#             db.session.add(cat)
#             db.session.commit()
#             cat_dict = cat.to_dict()
#             assert isinstance(cat_dict, dict) and cat_dict["name"] == "Test Category"
        
#             db.session.delete(cat)
#             db.session.commit()

# class TestProfile:
#     '''Profile model in models.py'''

#     def test_can_instantiate(self):
#         '''can be instantiated with a name.'''
#         profile = Profile(profile_picture="https://example.com/profile.jpg", bio="Test bio")
#         assert profile
    
#     def test_can_be_created(self):
#         '''can create records that can be committed to the database.'''
#         with app.app_context():
#             profile = Profile(profile_picture="https://example.com/profile.jpg", bio="Test bio")
#             db.session.add(profile)
#             db.session.commit()
#             assert profile.id

#             db.session.delete(profile)
#             db.session.commit()

#     def test_can_be_retrieved(self):
#         '''can be used to retrieve records from the database.'''
#         with app.app_context():
#             profile = Profile.query.all()
#             assert profile

#     def test_can_be_serialized(self):
#         '''can create records with a to_dict() method for serialization.'''
#         with app.app_context():
#             profile = Profile(profile_picture="https://example.com/profile.jpg", bio="Test bio")
#             db.session.add(profile)
#             db.session.commit()
#             profile_dict = profile.to_dict()
#             assert isinstance(profile_dict, dict) and profile_dict["bio"] == "Test bio"
        
#             db.session.delete(profile)
#             db.session.commit()

# class TestComment:
#     '''Comment model in models.py'''

#     def test_can_instantiate(self):
#         '''can be instantiated with a name.'''
#         comment = Comment(comment="Test comment")
#         assert comment
    
#     def test_can_be_created(self):
#         '''can create records that can be committed to the database.'''
#         with app.app_context():
#             comment = Comment(comment="Test comment")
#             db.session.add(comment)
#             db.session.commit()
#             assert comment.id

#             db.session.delete(comment)
#             db.session.commit()

#     def test_can_be_retrieved(self):
#         '''can be used to retrieve records from the database.'''
#         with app.app_context():
#             comment = Comment.query.all()
#             assert comment

#     def test_can_be_serialized(self):
#         '''can create records with a to_dict() method for serialization.'''
#         with app.app_context():
#             comment = Comment(comment="Test comment")
#             db.session.add(comment)
#             db.session.commit()
#             comment_dict = comment.to_dict()
#             assert isinstance(comment_dict, dict) and comment_dict["comment"] == "Test comment"
        
#             db.session.delete(comment)
#             db.session.commit()

# class TestWishlist:
#     '''Wishlist model in models.py'''

#     def test_can_instantiate(self):
#         '''can be instantiated with a name.'''
#         wishlist = Wishlist()
#         assert wishlist
    
#     def test_can_be_created(self):
#         '''can create records that can be committed to the database.'''
#         with app.app_context():
#             wishlist = Wishlist()
#             db.session.add(wishlist)
#             db.session.commit()
#             assert wishlist.id

#             db.session.delete(wishlist)
#             db.session.commit()

#     def test_can_be_retrieved(self):
#         '''can be used to retrieve records from the database.'''
#         with app.app_context():
#             wishlist = Wishlist.query.all()
#             assert wishlist

#     def test_can_be_serialized(self):
#         '''can create records with a to_dict() method for serialization.'''
#         with app.app_context():
#             wishlist = Wishlist()
#             db.session.add(wishlist)
#             db.session.commit()
#             wishlist_dict = wishlist.to_dict()
#             assert isinstance(wishlist_dict, dict)
        
#             db.session.delete(wishlist)
#             db.session.commit()

# class TestSubscription:
#     '''Subscription model in models.py'''

#     def test_can_instantiate(self):
#         '''can be instantiated with a name.'''
#         subscription = Subscription()
#         assert subscription
    
#     def test_can_be_created(self):
#         '''can create records that can be committed to the database.'''
#         with app.app_context():
#             subscription = Subscription()
#             db.session.add(subscription)
#             db.session.commit()
#             assert subscription.id

#             db.session.delete(subscription)
#             db.session.commit()

#     def test_can_be_retrieved(self):
#         '''can be used to retrieve records from the database.'''
#         with app.app_context():
#             subscription = Subscription.query.all()
#             assert subscription

#     def test_can_be_serialized(self):
#         '''can create records with a to_dict() method for serialization.'''
#         with app.app_context():
#             subscription = Subscription()
#             db.session.add(subscription)
#             db.session.commit()
#             subscription_dict = subscription.to_dict()
#             assert isinstance(subscription_dict, dict)
        
#             db.session.delete(subscription)
#             db.session.commit()

# class TestRecommendation:
#     '''Recommendation model in models.py'''

#     def test_can_instantiate(self):
#         '''can be instantiated with a name.'''
#         recommendation = Recommendation()
#         assert recommendation
    
#     def test_can_be_created(self):
#         '''can create records that can be committed to the database.'''
#         with app.app_context():
#             recommendation = Recommendation()
#             db.session.add(recommendation)
#             db.session.commit()
#             assert recommendation.id

#             db.session.delete(recommendation)
#             db.session.commit()

#     def test_can_be_retrieved(self):
#         '''can be used to retrieve records from the database.'''
#         with app.app_context():
#             recommendation = Recommendation.query.all()
#             assert recommendation

#     def test_can_be_serialized(self):
#         '''can create records with a to_dict() method for serialization.'''
#         with app.app_context():
#             recommendation = Recommendation()
#             db.session.add(recommendation)
#             db.session.commit()
#             recommendation_dict = recommendation.to_dict()
#             assert isinstance(recommendation_dict, dict)
        
#             db.session.delete(recommendation)
#             db.session.commit()


# # Similarly, you can write tests for other models like Category, Profile, Comment, Wishlist, Subscription, Recommendation.
