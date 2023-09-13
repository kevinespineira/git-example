import unittest

from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    # Add test cases here


if __name__ == '__main__':
    unittest.main()