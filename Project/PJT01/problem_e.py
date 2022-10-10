import json
import os

def dec_movies(movies):

    release_title = {} # 먼저 {개봉일:제목}을 빈 딕셔너리로 생성

    # 반복문 통해 movies 폴더 내부의 파일들을 오픈
    for i in os.listdir('data/movies'): # data/movies 폴더 내 파일들을 리스트형으로 추출 후 for문 돌려줌
        data_movie_jason = open(f'data/movies/{i}', encoding='utf-8')
        data_movie = json.load(data_movie_jason)

    # 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수 완성
        rls = data_movie.get('release_date') # 딕셔너리 형태의 data_movie에서 release_date 값을 rls로 지정
        ttl = data_movie.get('title') # 딕셔너리 형태의 data_movie에서 title 값을 ttl로 지정
        if rls[5:7] == '12': # rls 슬라이싱하여 월을 추출 후 '12'와 같으면 (문자열 '12'로 해야함. rls가 현재 문자열이기 때문)
            release_title[rls] = ttl # 처음에 생성했던 빈 딕셔너리에 key로 rls, value로 ttl을 넣음
    
    return release_title.values() # 완성된 딕셔너리 release_title에서 values값들만 return 함.

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))