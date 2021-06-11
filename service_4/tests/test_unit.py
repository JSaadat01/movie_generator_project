from unittest.mock import patch
from flask import url_for
from application import app
from flask_testing import TestCase

from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_movie(self):
        response = self.client.post(url_for('movie'), json={"location":"London 24", "weather":"Sunny 24"})
        self.assertEqual(b"Avengers: Infinity War 48", response.data)

