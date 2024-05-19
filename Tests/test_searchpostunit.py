import unittest
from Website import create_app, db
from Website.models import User, Post
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta

class SearchFunctionalityTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database
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

        # Create some test posts
        post1 = Post(title='Test Post 1', content='Content for test post 1', userId=self.user.id, date=datetime.now() - timedelta(days=1))
        post2 = Post(title='Another Post', content='Content for another post', userId=self.user.id, date=datetime.now() - timedelta(days=2))
        post3 = Post(title='Test Post 2', content='Content for test post 2', userId=self.user.id, date=datetime.now() - timedelta(days=3))
        db.session.add(post1)
        db.session.add(post2)
        db.session.add(post3)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_search_posts(self):
        with self.client:
            # Login as the test user
            self.client.post('/login', data=dict(
                email='testuser@example.com',
                password='TestPassword123!'
            ), follow_redirects=True)

            # Perform a search query for posts containing 'Test'
            response = self.client.post('/search', data=dict(
                search='Test'
            ), follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test Post 1', response.data)
            self.assertIn(b'Test Post 2', response.data)
            self.assertNotIn(b'Another Post', response.data)

if __name__ == '__main__':
    unittest.main()
