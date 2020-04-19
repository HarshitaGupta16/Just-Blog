from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm

posts = Blueprint('posts', __name__)  


"""
posts = [
    {
        'author': 'Harshita Gupta',
        'title': 'Blog Posts 1',
        'content': 'First post content',
        'date_posted': 'April 7, 2020'
    },
    {
        'author': 'Corey Schafer',
        'title': 'Blog Posts 2',
        'content': 'Second post content',
        'date_posted': 'April 8, 2020'
    }    
]
"""

@posts.route("/post/new",  methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)   #Here backref is author rather than user id
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/post/<int:post_id>")                                   #if user go to post/1 or post/2 this we change accordingly.
def post(post_id):
    post = Post.query.get_or_404(post_id)                           #it says give me the post with this id and if it doesn't exist then return a 404 which means page doesn't exist
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])  
@login_required                                 #if user go to post/1 or post/2 this we change accordingly.
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)                                                   #403 is a http response for a forbiddin route
    form = PostForm() 
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()                                        #we don't need to do db.session.add() bcz we are not adding something new, we are just updating
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])  #we only going to accept when they submit from that model so we dont need GET
@login_required                                 #if user go to post/1 or post/2 this we change accordingly.
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)    
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))





