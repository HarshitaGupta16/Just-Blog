from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)  

@main.route("/") 
@main.route ("/home")                                        #now we create a route, aroute is what we type in our browser to go to different pages.
def home():                                                 #login page, contact page all this we create using route decoraters.
    #return "Hello World!"                                  #decoraters adds additional functionality to existing functions. Here, main.route decorator will handle all complicated backend stuff.
    #return "<h1>Home page</h1>"                            #This will allow us write function that return the info that will be shown on our website for this route.
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)       # This forward slash "/" is the home page of the website.
                                                            #whatever variable name we choose to pass, we will have access to that variable in our template
                                                            #and this will be equal to this post data

                                                                
@main.route("/about")
def about():
    return render_template('about.html', title='About')