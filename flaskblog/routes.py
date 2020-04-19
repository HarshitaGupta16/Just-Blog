import os
import secrets
from PIL import Image                                  #from Pillow package which is used to resize uploaded image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt, mail
from flaskblog.forms import RegistrationForm, LoginForm,UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordFrom 
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

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








