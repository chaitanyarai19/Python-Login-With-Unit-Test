import unittest
from app import app

class TestLoginApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    
    def test_valid_login(self):
        response = self.app.post('/login', data=dict(username='user1', password='password1'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, user1', response.data)
    
    def test_invalid_login(self):
        response = self.app.post('/login', data=dict(username='user1', password='wrongpassword'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid login credentials', response.data)

if __name__ == '__main__':
    unittest.main()
