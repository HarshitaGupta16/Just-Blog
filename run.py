from flaskblog import create_app                            #When we import from package it is actually imported from __init__ file

app = create_app()

if __name__ == "__main__":                           #This file is only to run the application
    app.run(debug = True)                            #So we renamed it to run.py so that name does not conflit the name of the package