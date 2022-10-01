# Assignment: Unit test file for app.py
# https://flask.palletsprojects.com/en/1.1.x/quickstart/
# Date: 09/29/2022
# Author: derekYankie

from app import returnBackwardsString
from app import hello_world
import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.post('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)



    # # Unit tests defined for app.py
    # def test_hello(self):
    #     # Use Flask's test client for our test.
    #     self.test_app = app.test_client()
    #     # Make a test request to the Flask app
    #     response = self.test_app.post('/')
    #     # Assert response is 200 OK.
    #     self.assertEquals(response.status_code, "200 OK")
    #     self.app.post('/',follow_redirects=True)

    def test_return_backwards_string(self):
    # Test return backwards simple string
        random_string = "This is my test string"
        random_string_reversed = "gnirts tset ym si sihT"
        self.assertEqual(random_string_reversed, returnBackwardsString(random_string))

if __name__ == "__main__":
    unittest.main()