import requests


def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3' # BASE_URL : 불변 시 대문자로 작성
    PATH = '/movie/popular'
    my_params = {
        'api_key' : '55a806b044eebd05ba19b9855d6e8323',
        'language' : 'ko',
        'region' : 'KR',
    } # 딕셔너리로 넣어줘야 함('콜론'으로 key,value 값 적어줌)

    response = requests.get(BASE_URL + PATH, params=my_params).json() # requests 모듈 안에 get 메서드 사용
    result = response.get('results')
    return len(result)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
