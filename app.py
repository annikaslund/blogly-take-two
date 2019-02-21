"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
# db.create_all()


@app.route('/')
def redirect_to_home_page():
    """ On home page request, redirects to /users. """
    return redirect('/users')

@app.route('/users')
def generate_users_page():
    """ Generates unordered list of links to users. """
    users_data = User.query.all()
    return render_template('users.html', users=users_data)


@app.route('/users/<int:user_id>')
def display_single_user(user_id):
    """ Generates page for single user including photo """
    user_data = User.query.get(user_id)
    return render_template('user.html', profile_picture=user_data.image_url, first_name=user_data.first_name, last_name=user_data.last_name)