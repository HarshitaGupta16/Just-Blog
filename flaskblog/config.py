import os

class Config:                                               #when we use postgress then username and password gonna be in the connection string
                                                            #so we move the info in environment varible like we do in this class
    SECRET_KEY = 'f86a78015049060686a3141954b101f7'        #os.environ.get('SECRET_KEY')                           #'f86a78015049060686a3141954b101f7'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'                 #os.environ.get('SQLALCHEMY_DATABASE_URI')    #'sqlite:///site.db'        #for database
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'sign.of.happiness@gmail.com'                                        #os.environ.get('EMAIL_USER')
    MAIL_PASSWORD =  'sainath16'                                            #os.environ.get('EMAIL_PASS')