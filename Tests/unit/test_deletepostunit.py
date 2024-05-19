import unittest
from Website import create_app, db
from Website.models import User, Post
from werkzeug.security import generate_password_hash
from datetime import datetime

class DeletePostTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        cls.app.config['WTF_CSRF_ENABLED'] = False
        cls.client = cls.app.test_client()
        cls.ctx = cls.app.app_context()
        cls.ctx.push()

        # Mock the time_ago filter
        cls.app.jinja_env.filters['time_ago'] = cls.mock_time_ago

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        cls.ctx.pop()

    @staticmethod
    def mock_time_ago(date):
        now = datetime.now()
        diff = now - date

        if diff.days > 0:
            return f"{diff.days} days ago"
        elif diff.seconds > 3600:
            return f"{diff.seconds // 3600} hours ago"
        elif diff.seconds > 60:
            return f"{diff.seconds // 60} minutes ago"
        else:
            return "Just now"

    def setUp(self):
        db.create_all()

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
        self.post = Post(title='Test Post', content='Content for test post', userId=self.user.id)
        db.session.add(self.post)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_delete_post(self):
        with self.client:
            # Login as the test user
            self.client.post('/login', data=dict(
                email='testuser@example.com',
                password='TestPassword123!'
            ), follow_redirects=True)

            # Delete the post
            response = self.client.post('/delete', data=dict(
                postId=self.post.id
            ), follow_redirects=True)

            self.assertEqual(response.status_code, 200)

            # Verify that the post has been deleted
            deleted_post = Post.query.get(self.post.id)
            self.assertIsNone(deleted_post)

if __name__ == '__main__':
    unittest.main()
