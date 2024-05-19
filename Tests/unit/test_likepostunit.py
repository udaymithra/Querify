import unittest
from unittest.mock import patch
from flask import url_for, Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_login import login_required, login_user, current_user
from Website import create_app, db
from Website.models import User, Post, Likes, get_user_id

class LikePostTests(unittest.TestCase):

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
        db.session.query(Likes).delete()
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

        # Add a route for liking a post for the purpose of the test
        @self.app.route('/like', methods=['POST'])
        @login_required
        def like_post():
            post_id = request.form.get('postId')
            if not post_id:
                return jsonify({'error': 'No post ID provided'}), 400
            
            new_like = Likes(postId=post_id, userId=current_user.id)
            db.session.add(new_like)
            db.session.commit()
            return jsonify({'message': 'Post liked'}), 200

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    @patch('flask_login.utils._get_user')
    def test_like_post(self, mock_get_user):
        # Mock the current_user
        mock_get_user.return_value = self.user

        # Simulate liking a post by sending a POST request to the like endpoint
        response = self.client.post('/like', data=dict(
            postId=self.post.id
        ), follow_redirects=True)

        # Verify the post has been liked
        like = Likes.query.filter_by(postId=self.post.id, userId=self.user.id).first()
        self.assertIsNotNone(like)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
