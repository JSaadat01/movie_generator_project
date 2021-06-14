from application import app
from flask import request, Response
from random import choice

@app.route('/location', methods=["GET"])
def location():
    location = ['London 24','New Delhi 24','Tokyo 24', 'Bejing 24']
    return Response(choice(location), mimetype='text/plain')