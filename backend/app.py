from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from http import HTTPStatus
from controllers.users import Users, UserLogin, UserById, UserByToken, jwt
from controllers.recommendation import Recommendations, RecommendationByID
from controllers.subscription import Subscriptions, SubscriptionByID
from controllers.wishlist import Wishlists, WishlistByID
from controllers.category import Category, Categories, CategoryByID
from controllers.comment import Comments, CommentByID
from controllers.content import ContentByID, ContentCategory
from controllers.profile import Profiles, ProfileByID
from flask_cors import CORS
from flask_migrate import Migrate
from datetime import timedelta
from models import db, Category, Subscription, User, Content, Comment
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moringa-daily.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
app.config['SECRET_KEY'] = 'tvbubvhriefjkwerty='

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "maureenchelangat955@gmail.com"
app.config['MAIL_PASSWORD'] = "otvacdbrljoiviir"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

migrate = Migrate(app, db)

db.init_app(app)
jwt.init_app(app)

CORS(app)

api = Api(app)
mail = Mail(app)

def send_notification_email(user_email, content_title):
    sender = 'maureenchelangat955@gmail.com'
    msg = Message('New Content Available', sender=sender, recipients=[user_email])
    msg.body = f'There is a new content available: {content_title}. Check it out!'
    mail.send(msg)

def notify_admins(new_content):
    # Notify admins about the new content for approval
    admins = User.query.filter_by(role='ADMIN').all()
    for admin in admins:
        if admin:
            send_notification_email(admin.email, f'New Content: {new_content.title} for approval')

def notify_users(new_content):
    # Notify subscribers about the new content
    subscribers = Subscription.query.filter_by(category_id=new_content.category_id).all()
    for subscriber in subscribers:
        user = User.query.get(subscriber.user_id)
        if user:
            send_notification_email(user.email, new_content.title)

class Contents(Resource):

    def post(self):
        data = request.get_json()
        new_content = Content(
            title=data['title'],
            description=data['description'],
            content_type=data['content_type'],
            image_url=data['image_url'],
            user_id=data["user_id"],
            category_id=data['category_id']
        )
        db.session.add(new_content)
        db.session.commit() 

        notify_admins(new_content)
        notify_users(new_content)

        return make_response(jsonify({"message": "content created successfully"}), 200)

    def get(self):
        content_list = []
        for content in Content.query.all():
            user = User.query.filter_by(id=content.user_id).first()
            added_by = {}
            if user:
                added_by = {
                    "firstname": user.firstname,
                    "lastname": user.lastname,
                    "user_id": user.id
                }
            comments = Comment.query.filter_by(content_id=content.id).all()
            post_comments = []
            for comment in comments:
                user_comment = User.query.filter_by(id=comment.user_id).first()
                user_firstname = user_comment.firstname if user_comment else None
                post_comments.append({
                    "comment": comment.comment,
                    "user": user_firstname
                })
            content_dict = {
                "id": content.id,
                "title": content.title,
                "description": content.description,
                "content_type": content.content_type,
                "published_date": content.published_date,
                "image_url": content.image_url,
                "likes": content.likes,
                "dislikes": content.dislikes,
                "flagged": content.flagged,
                "public_status": content.public_status,
                "added_by": added_by,
                "category_id": [category.name for category in Category.query.filter_by(id=content.category_id)],
                "comments": post_comments
            }
            content_list.append(content_dict)
        return make_response(jsonify(content_list), 200)


class Home(Resource):
    def get(self):
        response_dict = {
            "Message": "Moringa School Daily API",
        }
        response = make_response(
            response_dict,
            HTTPStatus.OK,
        )
        return response

api.add_resource(Home, '/')
api.add_resource(Recommendations, '/recommendations')
api.add_resource(RecommendationByID, '/recommendations/<int:id>')
api.add_resource(Subscriptions, '/subscriptions')
api.add_resource(SubscriptionByID, '/subscriptions/<int:id>')
api.add_resource(Wishlists, '/wishlists')
api.add_resource(WishlistByID, '/wishlists/<int:id>')
api.add_resource(Users,'/users')
api.add_resource(UserLogin,'/login')
api.add_resource(UserById,'/users/<int:id>')
api.add_resource(UserByToken,'/user-token')

api.add_resource(Categories, '/categories')
api.add_resource(CategoryByID, '/categories/<int:id>')
api.add_resource(Comments, '/comments')
api.add_resource(CommentByID, '/comments/<int:id>')
api.add_resource(Contents, '/contents')
api.add_resource(ContentByID, '/contents/<int:id>')
api.add_resource(ContentCategory,'/contents/category/<int:id>')
api.add_resource(Profiles, '/profiles')
api.add_resource(ProfileByID, '/profiles/<int:id>')

if __name__=='__main__':
    app.run()