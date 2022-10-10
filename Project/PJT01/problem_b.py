import json
from pprint import pprint
from threading import get_ident

def movie_info(movie, genres):
    genre_ids = movie.get('genre_ids') # [18, 80] 
                
    new_movie_data = {
        'id' : movie.get('id'),
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_name' :[], # genre_ids 대신 genre_name을 출력해야 하기에 바꿔줌
    } 

    for genre_id in genre_ids: # [18, 80] 순서대로 for문 돌려줌
        for genre in genres: # genres의 딕셔너리 하나씩 뽑아냄
            if genre['id'] == genre_id: # genre 딕셔너리에서 ['id'] 뽑아내어 genre_id(18과 80)와 같으면
                new_movie_data['genre_name'].append(genre['name']) # genre 딕셔너리에서 ['name'] 뽑아내어 new_movie_data['genre_name']에 추가
    
    return new_movie_data

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))