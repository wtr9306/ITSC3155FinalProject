from flask import render_template, flash, redirect, url_for, abort
from app import app, db
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm, NewPostForm

@app.route('/')
@app.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Implement registration logic here
        flash('Registration successful')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Implement login logic here
        flash('Login successful')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        # Implement new post logic here
        flash('Post created')
        return redirect(url_for('index'))
    return render_template('new_post.html', title='New Post', form=form)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        abort(404)
    return render_template('show_post.html', post=post)