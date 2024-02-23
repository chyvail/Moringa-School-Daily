from flask import Flask
from faker import Faker
import random
from models import User, Content, Category, Comment, Profile, Recommendation, Subscription, Wishlist, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moringa-daily.db'
db.init_app(app)

fake = Faker()

def seed_data():
    image_urls = [
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXwWPGhCN2YY2wu9tCtYe5fhKe7XcJSrWqbA&usqp=CAU',
        'https://img.freepik.com/free-photo/medium-shot-man-wearing-vr-glasses_23-2149126949.jpg?size=626&ext=jpg',
        'https://img.freepik.com/free-photo/ai-nuclear-energy-future-innovation-disruptive-technology_53876-129784.jpg?size=626&ext=jpg',
        'https://img.freepik.com/free-photo/smiling-characters-holding-cable_1160-536.jpg?size=626&ext=jpg&ga=GA1.2.516349233.1708664809&semt=sph',
        'https://img.freepik.com/free-photo/cloud-computing-banner-background-smart-city_53876-108504.jpg?size=626&ext=jpg&ga=GA1.2.516349233.1708664809&semt=sph',
        'https://img.freepik.com/premium-photo/success-business-strategy-depicting-person-with-computer_124507-32320.jpg?size=626&ext=jpg&ga=GA1.2.516349233.1708664809&semt=sph'
    ]

    profile_picture_urls = [
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQv7l08_sO2B7_9VgXDy-gB56AsfzrBHpv4bA&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQGR3KoQjQLWagWihyrw1x2i6N2_Ic-ibkVQ&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSt-MBobPdLPK7rUSw9s49JQfqs_n2gbfb2hA&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQac_2ND3WQ2aJ0dYplynyWqLjtxQdImuu4fA&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvu8i0QEft4PdjT2IHFb-y80_KziAYzbhsCQ&usqp=CAU'
    ]

    with app.app_context():
        # Create users
        for _ in range(10):
            firstname = fake.first_name()
            lastname = fake.last_name()
            email = fake.email()
            password = fake.password()
            role = random.choice(['ADMIN', 'TECH-WRITER', 'USER'])
            user = User(firstname=firstname, lastname=lastname, email=email, password=password, role=role)
            db.session.add(user)
            # Create profile for each user
            profile_picture = random.choice(profile_picture_urls)
            bio = fake.text(max_nb_chars=200)
            profile = Profile(profile_picture=profile_picture, bio=bio, user_id=user.id)  # Pass user.id instead of user
            db.session.add(profile)

        # Create categories
        for _ in range(5):
            name = fake.word()
            category = Category(name=name)
            db.session.add(category)

        # Create contents
        for _ in range(20):
            title = fake.sentence()
            description = fake.paragraph()
            content_type = random.choice(['Article', 'Video', 'Podcast'])
            published_date = fake.date_time_this_year()
            image_url = random.choice(image_urls)
            likes = random.randint(0, 100)
            dislikes = random.randint(0, 50)
            flagged = fake.boolean()
            public_status = fake.boolean()
            user_id = random.randint(1, 10)
            category_id = random.randint(1, 5)
            content = Content(title=title, description=description, content_type=content_type,
                              published_date=published_date, image_url=image_url, likes=likes, dislikes=dislikes,
                              flagged=flagged, public_status=public_status, user_id=user_id, category_id=category_id)
            db.session.add(content)

        # Create comments
        for _ in range(30):
            comment_text = fake.text(max_nb_chars=100)
            user_id = random.randint(1, 10)
            content_id = random.randint(1, 20)
            comment = Comment(comment=comment_text, user_id=user_id, content_id=content_id)
            db.session.add(comment)

        # Create recommendations
        for content in Content.query.all():
            user_id = random.randint(1, 10)
            recommendation = Recommendation(content_id=content.id, user_id=user_id)  # Use content.id instead of content
            db.session.add(recommendation)

        # Create subscriptions
        for _ in range(20):
            category_id = random.randint(1, 5)
            user_id = random.randint(1, 10)
            subscription = Subscription(category_id=category_id, user_id=user_id)
            db.session.add(subscription)

        # Create wishlists
        for user in User.query.all():
            content_id = random.randint(1, 20)
            wishlist = Wishlist(content_id=content_id, user_id=user.id)  # Pass user.id instead of user
            db.session.add(wishlist)

        # Commit all changes
        db.session.commit()

if __name__ == '__main__':
    seed_data()
