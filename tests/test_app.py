import unittest
from app import app
from models import db

class UserRegistrationTestCase(unittest.TestCase):

    def setUp(self):
        app.config.from_object('config_test')  # Load the test configuration
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_registration(self):
        response = self.app.post('/register', json={"email": "test@example.com", "password": "test123"})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"User registered successfully", response.data)

if __name__ == '__main__':
    unittest.main()
