# config                    
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint     
# 
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_cors import CORS
# from flask_migrate import Migrate

# factory
def create_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     
    
    
    
    # from . import models 
    # models.db.init_app(app)
    # migrate = Migrate(app, models.db)

    # index route
    @app.route('/')
    def index(): 
        return render_template('index.html')
        # return 'Hello, PetFax!'

    # register pet blueprint 
    from . import pet 
    app.register_blueprint(pet.bp)

    # register fact blueprint 
    from . import fact
    app.register_blueprint(fact.bp)

    # return the app 
    return app