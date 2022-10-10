import json
from pprint import pprint

def movie_info(movie):
    movie_id = movie.get('id')  

    # movie 딕셔너리에서 get 함수를 사용하여 원하는 정보 추출하여 새로운 new_movie_data 생성
    new_movie_data = {
        'id' : movie_id,
        'title' : movie.get('title'),
        'poster_path' : movie.get('poster_path'),
        'vote_average' : movie.get('vote_average'),
        'overview' : movie.get('overview'),
        'genre_ids' : movie.get('genre_ids'),
    }  
    
    return new_movie_data

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
