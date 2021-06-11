from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.routes import Movies

from os import getenv
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=getenv("TEST_DATABASE_URI"),
            WTF_CSRF_ENABLED=False,
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestResponse(TestBase):

    def test_avengers(self):
        with requests_mock.mock() as m:
            m.get('http://movie-gen_location_service:5000/location', text='Tokyo 24')
            m.get('http://movie-gen_weather_service:5000/weather', text='Sunny 24')
            m.post('http://movie-gen_movie_service:5000/movie', text='Avengers 48')
            response = self.client.get(url_for('home'))
            self.assertIn(b'Avengers 48', response.data)
