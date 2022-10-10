# PJT 02

### 이번 pjt 를 통해 배운 내용

- 파이썬 자료형, 컨테이너, 제어문, 함수(메서드) 등을 종합한 프로젝트여서 개념을 잘 가지고 문제를 풀어야겠다 다짐을 하며 시작했고, 지난주보다는 개념이 좀 잡힌 상태여서 막히기도 했지만 해결방안을 차분히 생각해보며 진행했다.
- API를 이용한 첫 프로젝트! API가 많이 낯설긴 했지만 API와 인사하기 딱 좋은 프로젝트였다! 



## A. 인기 영화 조회

- 요구 사항 :

  * 인기 영화 목록 개수 출력

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * requests 라이브러리를 사용하여 TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청
    * 응답 받은 데이터의 영화 개수를 반환하는 함수 popular_count 완성

  ```python
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
  
  ```

  - 이 문제에서 어려웠던 점 : 
    * API 이용하는 것(BASE_URL, PATH, params 설정)
    * requests.get().json()
  - 내가 생각하는 이 문제의 포인트 : 위 두가지 내용의 정확한 이해 및 구현!

------

 

## B. 특정 조건에 맞는 인기 영화 조회1

- 요구 사항 :

  * 인기 영화 목록 중 평점이 8점 이상인 영화 목록 출력

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청
    * 응답 받은 데이터 중 평점(vote_average)이 8점 이상인 영화 목록을 반환하는 함수  vote_average_movies 완성
  
  ```python
  import requests
  from pprint import pprint
  
  
  def vote_average_movies():
      BASE_URL = 'https://api.themoviedb.org/3'
      PATH = '/movie/popular'
      my_params = {
          'api_key' : '55a806b044eebd05ba19b9855d6e8323',
          'language' : 'ko',
          'region' : 'KR',
      }
  
      response = requests.get(BASE_URL + PATH, params=my_params).json()
      movie_lists = response.get('results') # popular 영화목록 결과 추출
  
      good_movie_lists = []
      for movie_list in movie_lists:
        if movie_list['vote_average'] >= 8: # vote_average가 8 이상일 때
          good_movie_lists.append(movie_list) # good_movie에 append해줌
      return good_movie_lists
  
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      """
      popular 영화목록중 vote_average가 8 이상인 영화목록 반환
      (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
      """
      pprint(vote_average_movies())
      """
      [{'adult': False,
        'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
        'genre_ids': [28, 12, 878],
        'id': 634649,
        'original_language': 'en',
        'original_title': 'Spider-Man: No Way Home',
        'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                    '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                    '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                    '사상 최악의 위기를 맞게 되는데…',
        'popularity': 1842.592,
        'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
        'release_date': '2021-12-15',
        'title': '스파이더맨: 노 웨이 홈',
        'video': False,
        'vote_average': 8.1,
        'vote_count': 13954},
      ..생략..,
      }]
      """
  ```
  
  - 이 문제에서 어려웠던 점 : 
    * A 문제와 같음!  API & requests 하는 것!
    * 그 외 특이사항 없음
  - 내가 생각하는 이 문제의 포인트 : API & requests 하는 것!

------

 

## C. 특정 조건에 맞는 인기 영화 조회2

* 요구 사항: 
  * 인기 영화 목록을 평점이 높은 순으로 5개의 영화 데이터 목록 출력

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * TMDB에서 현재 인기있는 영화 목록(Get Popular) 데이터를 요청
    * 응답 받은 데이터 중 평점(vote_average)을 기준으로 평점이 높은 영화 5개 정보를 리스트로 반환하는 함수  ranking 완성
    * sort 메서드 혹은 sorted 함수의 특정 파라미터를 이용하기!

  ```python
  import requests
  from pprint import pprint
  
  from problem_b import vote_average_movies
  
  
  def ranking():
      BASE_URL = 'https://api.themoviedb.org/3'
      PATH = '/movie/popular'
      my_params = {
          'api_key' : '55a806b044eebd05ba19b9855d6e8323',
          'language' : 'ko',
          'region' : 'KR',
      }
  
      response = requests.get(BASE_URL + PATH, params=my_params).json()
      movie_lists = response.get('results') # popular 영화목록 결과 추출
  
      # sorted(<list>, key = <function>, reverse = True/False)
      # def lambda(x):
      #    return x['vote_average']
      new_movie_lists = sorted(movie_lists, key = lambda x : x['vote_average'], reverse=True) # vote_average가 높은 순으로 정렬
      rank5_movie_lists = list()
      for i in range(0, 5): # 상위 5개만 추출
        rank5_movie_lists.append(new_movie_lists[i])
      return rank5_movie_lists
  
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      """
      popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
      (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
      """
      pprint(ranking())
      """
      [{'adult': False,
        'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
        'genre_ids': [28, 18],
        'id': 361743,
        'original_language': 'en',
        'original_title': 'Top Gun: Maverick',
        'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                    '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                    '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                    '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
        'popularity': 911.817,
        'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
        'release_date': '2022-06-22',
        'title': '탑건: 매버릭',
        'video': False,
        'vote_average': 8.4,
        'vote_count': 1463},
      ..생략..,
      }]
      """
  ```
  
  - 이 문제에서 어려웠던 점 : 
    * vote_average 기준으로 내림차순 정렬할 때 간단히? 하려다 보니 람다함수를 사용하게 되었는데 람다함수 이해가 좀 어려웠던 것 같다. sorted(<list>, key = <function>, reverse = True/False) 
  - 내가 생각하는 이 문제의 포인트 
    * sorted(<list>, key = <function>, reverse = True/False) 하는 법!

------

 

## D. 특정 추천 영화 조회

* 요구 사항: 
  * 제공된 영화 제목(기생충, 그래비티, 검색할 수 없는 영화)을 검색하여 추천 영화 목록을 출력

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 제공된 영화 제목으로  TMDB에서 영화를 검색(Search Movies)
    * 응답 받은 결과 중 첫 번째 영화의 id값을 찾아 해당 영화에 대한 추천 영화 목록(Get Recommendations)을 가져옴
    * 추천 영화 목록 중 영화 제목만 출력하는 함수  recommendation 완성
  
  ```python
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
  
  ```
  
  - 이 문제에서 어려웠던 점 : 
    * params 내부에 query에 어떤 것을 넣어야 할지..
    * PATH에 변화 가능한 데이터({movie_id})를 넣을 때 f-string 사용해야겠다는 생각
  - 내가 생각하는 이 문제의 포인트 
    * query는 내가 찾을 값을 넣어주면 되었고
    * {movie_id} 이렇게 변화되는 값을 처리할 때는 한 번쯤  f-string을 생각해보자! 옆 짝꿍이 print('/movie/{movie_id}/recommendations') 해 보았는데 문자열로 프린트 되는 것을 보고 생각해냄!

------

 

## E. 출연진, 연출진 데이터 조회

* 요구 사항: 
  * 제공된 영화 제목(기생충, 검색할 수 없는 영화)을 검색하여 해당 영화의 출연진 그리고 스태프 중 연출진 목록만을 출력

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 제공된 영화 제목으로 TMDB에서 영화를 검색(Search Movies)
    * 응답 받은 결과 중 첫번째 영화의  id 값을 찾아 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옴
    * 출연진은  cast_id  값이 10 미만인 출연진만 추출하며, 연출진은 스태프 부서가 Directing인 데이터만 추출
    * 위 조건을 만족해서 답을 반환하는 함수 credits를 완성
  
  ```python
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
  ```
  
  - 이 문제에서 어려웠던 점 : 
    * response2에서 키값을 가져올 때 무작정 'results'를 가져왔는데 None값이 뜸.. API 확인해보고 'cast'라는 걸 깨달음.
    * 또 스태프 목록은 'cast'가 아니라 'crew'를 넣어야 나옴.. 'cast' 넣으면 스태프 목록 1명 뜸..
    * 'cast' 결과값 추출 이후에도 if movie_list3['known_for_department'] == 'Directing': 이라고 해서 엉뚱한 사람 한 명 더 뜸.. 여기서도 known_for_department이 아니라 department라는 걸 깨달음
  - 내가 생각하는 이 문제의 포인트 
    * 이 문제에서 3번이나 API를 잘 읽어야한다라는 걸 깨달음.. 가지고 온 정보니깐 다 맞는게 아니라 제대로 된 곳에서 가지고 온 것인지 똑바로 확인 또 확인해야함!!

------



# 후기

- 오늘 프로젝트는 내가 모르는 것을 한 번 더 짚고 넘어갈 수 있는 프로젝트였다. 지금은 좀 지쳐있지만 좀 시간이 지나고 나서 내가 몰랐던 람다함수나 오늘 배웠던 API 이용하여 정보 가져오는 것 등 복습하여 내 것으로 만드는 시간을 가져야겠다고 생각했다!
- 그렇게 생각할 수 있었던 이유는 그나마 개념이 적립되어서 내가 모르는 것을 뭔지 알 수 있기 때문에.. 저번주는 내가 모르는 것과 아는 것이 분간이 안 될 정도였는데..
- 그리고 시간을 가지고 차근차근히 하자! 그것이 내가 개발자가 되는 지름길!
