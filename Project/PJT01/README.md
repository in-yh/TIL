# PJT 01

### 이번 pjt 를 통해 배운 내용

- pjt가 이런거구나.. 너무 어렵게 생각해서 처음에 접근하는 것도 어려웠는데 내가 배운 거를 잘 이해하고 있다면 충분히 풀 수 있는 문제라고 생각하고 접근해야겠다는 생각이 들었다.
- 자료형,컨테이너에서 순회형으로 어떤걸 사용할 수 있는지, 슬라이싱 인덱스를 할 수 있는게 어떤건지, get()함수를 어디에 쓸 수 있는지 등 알고 있다고 생각했던 개념들이 모두 섞여서 pjt할 때는 혼란도 많았는데, 그 개념을 다시 복습으로 재적립하였고 문제를 차분히 이해하고 코딩을 해보니 프로그램은 정말 약속된 대로 움직이구나 라는 생각과 내가 짰던 코드들로 정답이 나올 때는 고생했던 만큼의 희열감을 느낄 수 있었다. 



## A. 제공되는 영화 데이터의 주요내용 수집

- 요구 사항 :

  * 샘플 영화 데이터(movie.json)가 주어지고 필요한 정보만 추출해 반환하는 함수를 완성

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * movie.json에서 id, title, poster_path, vote_average, overview, genre_ids키에 해당하는 값 추출
    * 추출한 값을 새로운 dictionary로 반환하는 함수 movie_info를 완성

  ```python
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
  ```

  - 이 문제에서 어려웠던 점 : 
    * get함수를 잘 이해하지 못한 상태로 문제를 풀다보니  get 함수는 어느 컨테이너든 다 쓸 수 있겠다는 잘못된 생각을 하게 되었고
    * 이후의 문제를 풀 때도 내장함수를 이용해서 풀려는 생각을 하게 되어 문제를 너무 어렵게 생각하게 되었다. 
  - 내가 생각하는 이 문제의 포인트 : get 함수의 정확한 이해!

------

 

## B. 제공되는 영화 데이터의 주요내용 수정

- 요구 사항 :

  * 이전 단계에서 만들었던 데이터 중 genre_ids를 장르 번호가 아닌 장르 이름 리스트 genre_names로 바꿔 반환하는 함수 완성

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * movie.json에서 id, title, poster_path, vote_average, overview, genre_ids키에 해당하는 값 추출
    * genres.json을 이용하여 genre_ids를 각 장르 번호에 맞는 name값으로 대체한 genre_names 키를 생성
    * 새로운 dictionary를 반환하는 함수 movie_info를 완성

  ```python
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
  ```

  - 이 문제에서 어려웠던 점 : 
    * genre_ids([18, 80])를 for문을 돌려야겠다 생각은 했는데 for genre_id in genre_ids로 간단히 생각을 못했다. 처음에는 for i in range(len(genre_ids)) 이런식으로 했음..;;(여기서 리스트를 for문 돌릴 때의 개념 다시 적립!)
    * 마찬가지로 for genre in genres를 사용해서 이렇게 간단하게 genres리스트에서 딕셔너리 하나씩을 뽑아내다니..
    * append할 때도 a = a.append(genre['name'])로 했음.. ('a='을 빼야함) append는 그냥 추가하면 되는거지 다시 a에 할당하는 것이 아닌 것을 확인함. 심지어는 계속 오류 떠서 append()가 아니라 append[]인가라는 생각까지.. 오류 뜨면 머리가 너무 혼란,복잡.. 무엇이 잘못인지도 정확히 판단이 안됨..ㅠㅠ
  - 내가 생각하는 이 문제의 포인트 : 리스트 형태 for 문 돌릴 때 어렵게 생각하지 말기!

------

 

## C. 다중 데이터 분석 및 수정

* 요구 사항: 
  * movies.json에는 평점이 높은 20개의 영화 데이터가 주어진다.
  * 이 중 서비스 구성에 필요한 정보만 추출해 반환하는 함수 완성

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 이전 단계 함수 구조 재사용
    * 개별 영화 데이터는  id, title, poster_path, vote_average, overview, genre_names 키에 해당하는 값 추출
    * 새로운 list를 반환하는 함수 movie_info를 완성

  ```python
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
  ```

  - 이 문제에서 어려웠던 점 : 
    * B에서는 하나의 데이터를 분석했지만 C에서는 여러개의 데이터를 분석해야 했는데, B단계에서의 하나의 데이터는 딕셔너리 형태였고 C에서는 여러개의 딕셔너리 데이터가 리스트로 묶여 있었다. 그래서 C에서는 get함수를 사용할 수 없었다. 그러면 어떻게 해야하나 고민을 해보았을 때.. 
  - 내가 생각하는 이 문제의 포인트 
    * 리스트 형태의 다중 데이터를 for문을 돌려서 하나의 딕셔너리씩 뽑아내어보자 라는 생각을 하게됨!
    * 이 때부터 잘 풀리기 시작했고 생각을 하고 푸니 프로그램도 잘 돌아가는구나 경험을 하게됨! 내가 이것을 실행시키기 위해서 생각?전략?이 필요하다는 것을 느낌! 무조건 돌진하는 것이 아니라!

------

 

## D. 알고리즘을 사용한 데이터 출력

* 요구 사항: 
  * 영화 세부 정보 중 수입 정보(revenue)를 이용하여 모든 영화 중 가장 높은 수익을 낸 영화 출력

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 반복문 통해 movies 폴더 내부의 파일들을 오픈
    * 수익이 가장 높은 영화의 제목을 출력하는 함수 max_revenue를 완성

  ```python
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
  ```

  - 이 문제에서 어려웠던 점 : 
    * 폴더 내부 파일들 오픈하는 것
    * for문을 돌려 폴더 내부 파일들을 오픈할 때 '범위'를 어떻게 설정할 것인지
  - 내가 생각하는 이 문제의 포인트 
    * 폴더 내부 파일들 오픈하는 것은 아래 주어진 코드를 착안하여 수행했다. 대신 for문으로 열어야 하기에 폴더 내부 파일을 이름은 {i}라는 변수로 설정했음.
    * for문을 돌릴 때 범위 설정은 google 검색을 통해 os 모듈 내 listdir함수를 활용하였다. 폴더 내 파일들을 리스트형으로 추출해주는 함수라고 함.

------

 

## E. 알고리즘을 사용한 데이터 출력

* 요구 사항: 
  * 영화 세부 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉한 영화들의 제목 리스트를 출력하는 알고리즘 작성

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 반복문 통해 movies 폴더 내부의 파일들을 오픈
    * 개봉일이 12월인 영화들의 제목을 리스트로 출력하는 함수 dec_movies 완성

  ```python
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
  ```

  - 이 문제에서 어려웠던 점 : 
    * if문으로 개봉일이 12월인 영화를 추출하려고 했는데, 개봉일을 슬라이싱 인덱스를 활용하였음.(분명 월을 추출하는 다른 방법이 있을텐데, 일단 쉽게 생각해봤음..) 
  - 내가 생각하는 이 문제의 포인트 
    * 개봉일이 12월인 영화를 추출할 때 if문을 사용하는 것
    * date에서 '월'만을 추출하는 방법

------



# 후기

- 오늘 프로젝트는 시작이 너무 어려웠다. 그러나 시작을 해보니 '별거 아니였구나' 라는 생각을 했는데 여기서 두 가지 생각이 들었다.
- 첫 번째는 시작을 너무 거창하게 어렵게 생각하지 말 것과
- 두 번째는 내가 이미 정답을 봐서 쉬워보이는 것일수도 있으니 방심하지 말고 다시 문제만 보고 풀 수 있는지 연습을 해보자라는 것
- 근데 이미 일요일 12시네..ㅎ 언제 쉬지.. 다음주 또 다시 달릴려면 좀 쉼이 필요할 것 같다 ㅎㅎ 쉬었다가 시험 준비하면서 다시 돌아온다 I'll be back.. 
