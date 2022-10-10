import json
import os

def max_revenue(movies):
    
    revenue_title = dict() # 먼저 {수입:제목}을 빈 딕셔너리로 생성

    # 반복문 통해 movies 폴더 내부의 파일들을 오픈
    for i in os.listdir('data/movies'): # data/movies 폴더 내 파일들을 리스트형으로 추출 후 for문 돌려줌
        data_movie_jason = open(f'data/movies/{i}', encoding='utf-8') # 순서대로 파일 오픈
        data_movie = json.load(data_movie_jason) # 파일을 우리가 읽을 수 있게 로드
        rvn = data_movie.get('revenue') # 딕셔너리 형태의 data_movie에서 revenue 값을 rvn으로 지정 
        ttl = data_movie.get('title') # 딕셔너리 형태의 data_movie에서 title 값을 ttl로 지정 
        revenue_title[rvn] = ttl # 처음에 생성했던 빈 딕셔너리에 key로 rvn, value로 ttl을 넣음

    # 수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue를 완성
    return revenue_title[max(revenue_title)] # max함수를 통해 revenue_title에서 가장 높은 key값을 추출 후, 그 key값을 인덱싱하여 value값을 return함.
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))