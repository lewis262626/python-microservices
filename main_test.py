import os
import unittest
from main import app
from main import persons
from flask import json

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG']   = False
        self.app = app.test_client()

    # tests
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_persons_response(self):
        response = self.app.get('/persons')
        data = json.loads(response.data)
        self.assertEqual(data, persons)

if __name__ == "__main__":
    unittest.main()