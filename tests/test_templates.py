import unittest
from flask import Flask, render_template
from app import create_app

class TestTemplates(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_base_template(self):
        with self.app.test_request_context():
            rendered = render_template('base.html')
            self.assertIn(b'<title>{% block title %}{% endblock %}</title>', rendered)
            self.assertIn(b'<link rel="stylesheet" href="{{ url_for(\'static\', filename=\'style.css\') }}">', rendered)

    def test_index_template(self):
        with self.app.test_request_context():
            rendered = render_template('index.html')
            self.assertIn(b'<h1>Welcome to my app</h1>', rendered)
            self.assertIn(b'<p>This is a sample Python web app for a Git workshop.</p>', rendered)