from application import app
from flask import request, Response
from random import choice

@app.route('/weather', methods=["GET"])
def weather():
    weather = ['Sunny 24','Rainy 24','Windy 24',]
    return Response(choice(weather), mimetype='text/plain')