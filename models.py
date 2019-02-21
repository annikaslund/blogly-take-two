"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """ Connect to database. """

    db.app = app
    db.init_app(app)


class User(db.Model):
    """ User. """ 

    __tablename__ = "users"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.String(30),
                    nullable=False)
    last_name = db.Column(db.String(30),
                    nullable=False)
    image_url = db.Column(db.String(200),
                    nullable=True,
                    default='https://www.top13.net/wp-content/uploads/2015/10/perfectly-timed-cat-photos-funny-cover.jpg')


class Post(db.Model):
    """ Post """ 

    __tablename__ = "posts"
    user = db.relationship('User', backref='posts')

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    title = db.Column(db.String(50),
                    nullable=True,
                    default='Untitled')
    content = db.Column(db.Text,
                    nullable=False)
    created_at = db.Column(db.DateTime,
                    nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)


class UserPost(db.Model):
    """ User Posts """

    __tablename__ = "user_posts"
    
    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    user_id = db.Column(db.Integer,
                    db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,
                    db.ForeignKey('posts.id'))