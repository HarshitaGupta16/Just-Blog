import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)                           #8 is number of bytes
    _, f_ext = os.path.splitext(form_picture.filename)         #Store both filename and extension, common way in python to throw away the variable name in python is to put underscore as variable name
    picture_fn = random_hex + f_ext                            #complete file name stored in picture_fn
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()                                     #Leave it empty as we have kept default as 1800 second expiration time
    msg = Message('Password Reset Request', sender='noreply@demo.com', reply_to=None, recipients=[user.email]) #don't try to spoof the sender(prentending to be somebody u r not)
                                           # _external =it is to get an absolute url rather than a relative url bcz link in email needs to have full domain depending on how complex email is
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    #mail.send(msg)