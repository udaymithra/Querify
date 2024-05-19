import unittest
from unittest.mock import patch
from Website import create_app, db
from Website.models import User
from werkzeug.security import generate_password_hash

class UserLoginTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/database.db'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

        # Create a test user for login
        user = User(
            firstName='Test',
            lastName='User',
            emailAddress='testuser_login@example.com',  # Use a unique email for this test
            password=generate_password_hash('TestPassword123!', method='pbkdf2:sha256')
        )
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    @patch('Website.auth.render_template')
    @patch('Website.views.render_template')
    def test_user_login(self, mock_views_render_template, mock_auth_render_template):
        mock_auth_render_template.return_value = 'Mocked Login Page'
        mock_views_render_template.return_value = 'Mocked Home Page'
        response = self.client.post('/login', data=dict(
            email='testuser_login@example.com',
            password='TestPassword123!'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mocked Home Page', response.data)

if __name__ == '__main__':
    unittest.main()
