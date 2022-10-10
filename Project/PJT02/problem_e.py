import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    PATH = '/search/movie'
    my_params = {
        'api_key' : '55a806b044eebd05ba19b9855d6e8323',
        'language' : 'ko',
        'query' : title,
    }

    response = requests.get(BASE_URL + PATH, params=my_params).json() 
    movie_lists = response.get('results')

    if movie_lists == []:
        return None
    else:
        movie_id = movie_lists[0]['id'] 
        PATH2 = f'/movie/{movie_id}/credits'
        my_params2 = {
            'api_key' : '55a806b044eebd05ba19b9855d6e8323',
            'language' : 'ko',
        }

        response2 = requests.get(BASE_URL + PATH2, params=my_params2).json()
        movie_lists2 = response2.get('cast') # cast의 결과값 추출!! api 예시 확인 잘 해야함..!!
        
        cast = []
        for movie_list2 in movie_lists2:
            if movie_list2['cast_id'] < 10:
                cast.append(movie_list2['name'])

        movie_lists3 = response2.get('crew') # cast로 넣으면 안되고 crew 넣어야 함!! api 예시 확인 잘 해야함..!!

        directing = []
        for movie_list3 in movie_lists3:
            if movie_list3['department'] == 'Directing': # known_for_department로 넣으면 안되고 department로 넣어야 함!! api 예시 확인 잘 해야함..!!
                if movie_list3['name'] in directing: # 중복 피하기 위한 문구
                    pass
                elif movie_list3['name'] not in directing:
                    directing.append(movie_list3['name'])

        result = dict(cast = cast, directing = directing)
        return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
