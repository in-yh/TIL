import json
from pprint import pprint

def movie_info(movies, genres):

    my_movies = list() # 먼저 반환값을 빈리스트로 설정

    for movie in movies: # movies 리스트에서 리스트 내 딕셔너리 하나씩 뽑아냄
        genre_ids = movie.get('genre_ids') 
        
        new_movie_data = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_name' :[],
    }

        for genre_id in genre_ids: 
            for genre in genres:
                if genre['id'] == genre_id:
                    new_movie_data['genre_name'].append(genre['name'])
    
        my_movies.append(new_movie_data) # 추출된 데이터를 my_movies 리스트에 추가함

    return my_movies

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
