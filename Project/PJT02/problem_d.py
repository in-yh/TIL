import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/search/movie'
    my_params = {
        'api_key' : '55a806b044eebd05ba19b9855d6e8323',
        'language' : 'ko',
        'query' : title, # 찾을 값(title)을 적는다.
        'region' : 'KR',
    }

    response = requests.get(BASE_URL + PATH, params=my_params).json()
    movie_lists = response.get('results') # 'title=기생충'인 리스트 추출

    if movie_lists == []: # '검색할 수 없는 영화'일 때
        return None
    else: # movie_lists가 있을 때, 검색 가능할 때
        movie_id = movie_lists[0]['id'] # 'title=기생충'인 리스트의 첫 id 추출

        PATH2 = f'/movie/{movie_id}/recommendations' # f-string으로 쓰기!! 해결하기 위해 오래걸림..ㅠㅠ
        my_params2 = {
            'api_key' : '55a806b044eebd05ba19b9855d6e8323',
            'language' : 'ko',
        }

        response2 = requests.get(BASE_URL + PATH2, params=my_params2).json() 
        movie_lists2 = response2.get('results') # movie_id에 따라 영화 목록 재추출

        recommend_movie = []
        for movie_list2 in movie_lists2: # 영화 목록 for문 돌려서 title만 추출
            recommend_movie.append(movie_list2['title'])
    
        return recommend_movie

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
