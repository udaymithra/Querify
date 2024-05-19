import unittest
from unittest.mock import patch
from Website import create_app, db

class UserSignupTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/database.db'
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    @patch('Website.auth.render_template')
    @patch('Website.views.render_template')
    def test_user_signup(self, mock_views_render_template, mock_auth_render_template):
        mock_auth_render_template.return_value = 'Mocked Signup Page'
        mock_views_render_template.return_value = 'Mocked Home Page'
        response = self.client.post('/signup', data=dict(
            firstName='Test',
            lastName='User',
            email='testuser_signup@example.com',  # Use a unique email for this test
            password1='TestPassword123!',
            password2='TestPassword123!'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mocked Home Page', response.data)

if __name__ == '__main__':
    unittest.main()
