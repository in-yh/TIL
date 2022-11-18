import requests
import json

api_key = '87b98e5ba758dcfaea8c1b1917b6112c'

def get_genre():
    genre_data = []
    request_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US'
    genre= requests.get(request_url).json()
    genres = genre['genres']
    for genre_1 in genres:
        fields = {
            'id' : genre_1['id'],
            'name' : genre_1['name'],
        }

        data = {
            "pk": genre_1['id'],
            "model": "movies.genre",
            "fields": fields
        }

        genre_data.append(data)

    with open("genre.json", "w", encoding="utf-8") as w:
        json.dump(genre_data, w, indent="  ", ensure_ascii=False)

get_genre()