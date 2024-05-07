from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME='database.db'
# Improved configuration (consider using environment variables)
app_config = {
    'SECRET_KEY': 'heqpoc gadjhhjhj',  # Replace with a strong secret key
    'SQLALCHEMY_DATABASE_URI': f'sqlite:///{DB_NAME}',  # Replace DB_NAME with your filename
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
}

def create_app():
    app = Flask(__name__)
    app.config.update(app_config)
    


    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Post

    # Create tables outside the context for reliable execution
    with app.app_context():
        db.create_all()
        print("--- Creating....->")
        print("Database tables created successfully!")
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app