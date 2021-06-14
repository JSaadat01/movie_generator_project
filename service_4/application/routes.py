from application import app
from flask import request, Response

@app.route('/movie', methods=["POST"])
def movie():
    movies = {
    "London 24" : {"Sunny 24" : "Avengers: Infinity War 48", "Rainy 24" : "Schindler's List 48", "Windy 24" : "The Shawshank Redemption 48", "Foggy 24" : "The Croods 48"}
    "New Delhi 24" : {"Sunny 24" : "Khaali Peeli 48", "Rainy 24" : "Bulbbul 48", "Windy 24" : "Devdas 48", "Foggy 24" : "How To Train Your Dragon 48"}
    "Tokyo 24" : {"Sunny 24" : "Rurouni Kenshin 48", "Rainy 24" : "Ring 48", "Windy 24" : "Midnight Sun 48", "Foggy 24" : "Despicable Me 48"}
    }
    info = request.json 
    return Response(movies[info["location"]][info["weather"]], mimetype='text/plain')