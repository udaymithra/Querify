from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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
    
    
    return app