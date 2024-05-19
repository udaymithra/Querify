import unittest
from unittest.mock import patch
from flask import url_for, Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_login import login_required, login_user, current_user
from Website import create_app, db
from Website.models import User, Post, Comments, get_user_id
from datetime import datetime
import pytz

class CommentPostTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/test.db'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

        # Clear any existing data
        db.session.query(Comments).delete()
        db.session.query(Post).delete()
        db.session.query(User).delete()
        db.session.commit()

        # Create a test user
        self.user = User(
            firstName='Test',
            lastName='User',
            emailAddress='testuser@example.com',
            password=generate_password_hash('TestPassword123!', method='pbkdf2:sha256')
        )
        db.session.add(self.user)
        db.session.commit()

        # Create a test post
        self.post = Post(
            userId=self.user.id,
            title='Test Post',
            content='Content for test post'
        )
        db.session.add(self.post)
        db.session.commit()

        # Add a route for commenting on a post for the purpose of the test
        @self.app.route('/comment', methods=['POST'])
        @login_required
        def comment_post():
            data = request.form
            post_id = data.get('postId')
            comment_content = data.get('comment')

            if not post_id or not comment_content:
                return jsonify({'error': 'Post ID and comment content are required'}), 400

            perth_tz = pytz.timezone('Australia/Perth')
            utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
            now_user_region = utc_now.astimezone(perth_tz)
            
            new_comment = Comments(
                userId=current_user.id,
                postId=post_id,
                content=comment_content,
                date=now_user_region
            )
            db.session.add(new_comment)
            db.session.commit()
            return jsonify({'message': 'Comment added'}), 200

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    @patch('flask_login.utils._get_user')
    def test_comment_post(self, mock_get_user):
        # Mock the current_user
        mock_get_user.return_value = self.user

        # Simulate commenting on a post by sending a POST request to the comment endpoint
        response = self.client.post('/comment', data=dict(
            postId=self.post.id,
            comment='This is a test comment'
        ), follow_redirects=True)

        # Verify the comment has been added
        comment = Comments.query.filter_by(postId=self.post.id, userId=self.user.id).first()
        self.assertIsNotNone(comment)
        self.assertEqual(comment.content, 'This is a test comment')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
