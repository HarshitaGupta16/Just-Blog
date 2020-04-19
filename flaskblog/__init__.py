from flask import Flask           #Flask is a class
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


                                                    


db = SQLAlchemy()                                         #SQL alchemy database instance
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'               #info class in bootstrap is colored blue information alert

mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)                                       #This is imported by run.py
                                                            #app is a variable and setting this as instance of Flask class
                                                            #__name__ is a special variable in python, it is just the name of module
                                                            #if we run the python script directly then __name__ can be equal to __name__
                                                            #now we have instanciated flask application in this app variable.
    app.config.from_object(Config)    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    
    from flaskblog.users.routes import users              #first users is the package and latter is instance of Blueprint class
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app