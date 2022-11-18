import requests
import json

api_key = '87b98e5ba758dcfaea8c1b1917b6112c'

movie_id_list = []
# movie id 값이 담긴 리스트

for page in range(1,201):
    request_url_movie = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page={page}'
    movie = requests.get(request_url_movie).json()
    result = movie.get('results')
    for i in range(len(result)):
        movie_id_list.append(result[i]['id'])


def get_movie_detail():
    detail_data = []
    for movie_id in movie_id_list:
        request_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US'
        details = requests.get(request_url).json()
        if details.get('production_countries', ''):

            fields = {
                'backdrop_path' : details['backdrop_path'],
                'id' : details['id'],
                'production_countries' : details['production_countries'][0]['name']
            }

            data = {
                "pk": details['id'],
                "model": "movies.movie",
                "fields": fields
            }

            detail_data.append(data)

        with open("movie_detail.json", "w", encoding="utf-8") as w:
            json.dump(detail_data, w, indent="\\t", ensure_ascii=False)

get_movie_detail()