import unittest
from unittest.mock import patch
from Website import create_app, db

class HomePageTests(unittest.TestCase):

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

    @patch('Website.views.render_template')
    def test_home_page(self, mock_render_template):
        mock_render_template.return_value = 'Mocked Home Page'
        response = self.client.get('/')
        self.assertIn(response.status_code, [200, 302])
        if response.status_code == 302:
            self.assertTrue('/login' in response.headers['Location'])

if __name__ == '__main__':
    unittest.main()
