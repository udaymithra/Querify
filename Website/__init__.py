from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_humanize import Humanize

# Initialize the extension
humanize = Humanize()

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
    socketio = SocketIO(app)
    

    humanize.init_app(app)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Post
    from .views import likes_count_by_id,update_count_by_id,delete_count_by_id,like_count_of_comment_by_id,update_comment_count_by_id,delete_comment_count_by_id
    # Create tables outside the context for reliable execution
    with app.app_context():
        # Creating a Database
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    # Post Like and Dislike Functionality
    @socketio.on('like_update_count')
    def like_update_count(data):
        post_id = data.get('post_id')  # Assuming data contains 'post_id' key
        new_count = likes_count_by_id(post_id) + 1  # Example increment
        update_count_by_id(post_id)
        socketio.emit('like_count_updated', {'post_id': post_id, 'count': new_count})

    @socketio.on('dislike_update_count')
    def dislike_update_count(data):
        post_id = data.get('post_id')
        deleted=delete_count_by_id(post_id)
        if deleted:
            new_count=likes_count_by_id(post_id)
            socketio.emit('dislike_count_updated', {'post_id': post_id, 'count': new_count})
        else:
            socketio.emit('dislike_count_updated', {'post_id': post_id, 'count': 0})
    #Comment Like and Dislike Functionality
    @socketio.on('like_update_comment_count')
    def like_update_comment_count(data):
        user_id = data.get('user_id') 
        comment_id=data.get('comment_id')
        new_count = like_count_of_comment_by_id(user_id,comment_id) + 1  # Example increment
        update_comment_count_by_id(user_id,comment_id)
        socketio.emit('like_update_comment_count', {'comment_id':comment_id , 'count': new_count})

    @socketio.on('dislike_update_comment_count')
    def dislike_update_comment_count(data):
        user_id = data.get('user_id') 
        comment_id=data.get('comment_id')
        deleted=delete_comment_count_by_id(user_id,comment_id)
        if deleted:
            new_count=like_count_of_comment_by_id(user_id,comment_id)
            socketio.emit('dislike_update_comment_count', {'comment_id': comment_id, 'count': new_count})
        else:
            socketio.emit('dislike_update_comment_count', {'comment_id': comment_id, 'count': 0})



    return app
    