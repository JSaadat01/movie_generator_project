from unittest.mock import patch
from flask import url_for
from application import app
from flask_testing import TestCase

from os import getenv

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_weather(self):
        for i in range(50):
            response = self.client.get(url_for('weather'))
            self.assertIn(response.data, [b"Sunny 24", b"Rainy 24", b"Windy 24"])
