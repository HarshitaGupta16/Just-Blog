from datetime import datetime
from flaskblog import db, login_manager

class User(db.Model):                                                            #user class to hold users, UserMixin class include method is_authenticated, is_active, is_anonymous, get_id
    id = db.Column(db.Integer, primary_key=True)                             #id is a primary key
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')            #profile pic can be same like if it is default so it can't be unique
    password = db.Column(db.String(60), nullable=False)                                     #people can have same passwords
    posts = db.relationship('Post', backref='author', lazy=True)
    #post attribute has a relationship to the Post model, backref is similar to adding column to the post model.
    #When we have a post, we can simply use this authorattribute to get the user who created the post, this is done be backref
    #lazy arg just defines sql alchemy loads the data from database in one go

    def __repr__(self):                                                                    
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #default is taken beacuse if no date is specified then it will take the current time so we take datetime module
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):                                                                    
        return f"Post('{self.title}', '{self.date_posted}')"  #this will be printed out as Post
        
        #we are not adding authors to post model because post model and user model will have a relationship, users will author post.
        #This is a one to many relationship, bcz one user can have multiple post but a post can ave only one author 
#Now by these 2 above database models we will create database by using command line