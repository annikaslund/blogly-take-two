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
def generate_user_page():
    """ Generates unordered list of links to users. """

    return render_template('users.html')