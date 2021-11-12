from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager =LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'


def create_app(config_name):
    app = Flask(__name__)
    
     # initializing flask extension
    bootstrap.init_app(app)
    db.init_app(app)
  
    
    # creating app configurations
    app.config.from_object(config_options[config_name])
    
    #registering blueprints
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    
    return app
    
    
