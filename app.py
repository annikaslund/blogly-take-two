"""Blogly application."""

from flask import Flask, render_template, request, redirect
from models import db, connect_db, User, Post
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "a"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

debug = DebugToolbarExtension(app)
db.create_all()


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
    return render_template('user.html', user=user_data)


@app.route('/users/new')
def show_create_user_form():
    """Show form to create a new user"""
    return render_template('add_new_user.html')


@app.route('/users', methods=["POST"])
def submit_create_user_form():
    """Submit form to create a new user"""

    first_name = request.form['first-name-input']
    last_name = request.form['last-name-input']
    image = request.form['img-url-input'] or None

    new_user = User(first_name=first_name,
                    last_name=last_name,
                    image_url=image)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/edit')
def show_edit_user_page(user_id):
    """ Show form to edit an existing user. """
    user_data = User.query.get(user_id)

    return render_template('edit_user.html', user=user_data)


@app.route('/users/<int:user_id>/edit', methods=["POST"])
def save_edited_user(user_id):
    """ On home page request, redirects to /users. """
    user = User.query.get(user_id)

    user.first_name = request.form['first-name-input']
    user.last_name = request.form['last-name-input']
    user.image_url = request.form['img-url-input']

    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """Deletes user and redirects to main /users page"""
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
   
    return redirect('/users')


@app.route('/users/<int:user_id>/posts/new')
def show_new_post_form(user_id):
    """ Shows a form to create a new post for an existing user. """
    user = User.query.get(user_id)

    return render_template('create_post.html', user=user)


@app.route('/users/<int:user_id>/posts', methods=["POST"])
def add_new_post(user_id):
    """ Adds new post to user page. """

    title = request.form['title-input']
    content = request.form['content-input']

    new_post = Post(title=title,
                    content=content,
                    user_id=user_id)

    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/users/{user_id}')


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    """ Function presents single post """

    post = Post.query.get(post_id)

    return render_template('post.html', post=post)