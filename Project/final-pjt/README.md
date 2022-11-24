# FINAL-PJT



## A. 컨셉

* Word Cloud (워드 클라우드)
  * 키워드, 개념 등을 직관적으로 파악할 수 있도록 핵심 단어를 시각적으로 돋보이게 하는 기법

* 'Word Cloud'를 사용해 영화 정보와 관련된 키워드를 시각적으로 보여주고, 사용자가 선택한 키워드에 Fit한 영화를 추천해주는 사이트



## B. 타겟 유저 & 제안 배경

* 타겟 유저 

  * OTT 채널에서 선택지가 너무 많아 어떤 영화를 검색하고 봐야할지 선택하지 못 하는 사람
  * 능동적으로 정보를 탐색하는 것이 아닌 수동적으로 탐색하는 유저

* 제안 배경

  * 정보 과잉 시대에서 단순한 선택 프로세스와 간단한 추천 서비스에 대한 수요 있다고 판단

  * '햄릿 증후군'. 즉, 선택 장애를 앓고 있는 개인의 비율 증가

  * 타인에 의한 선택이 나의 선택이 되는 큐레이션 서비스의 호황

    -> 빈도수, 평점 등 유의미한 지표 통해 글자 크기 변화시키고, 큰 글자를 권유한다는 느낌을 줌. 시각화를 통한 추천 서비스 제공




## C. 모델링 ERD

![캡처](https://user-images.githubusercontent.com/109324632/203733130-f065ba8b-c6d7-443f-898e-f687b147c763.PNG)



* TMDB API에서 genre, popular, detail 목록 크롤링하여 데이터 수집(약 4000개 영화 데이터)
  * detail 데이터는 detail 모델에 저장
  * genre 데이터는 genre 모델에 저장
  * popular 데이터는 movie 모델에 저장
    * 영화와 장르는 M:N 관계 설정(하나의 영화에 여러 장르가 포함될 수도 있고, 하나의 장르에 여러 영화가 있을 수 있으므로)
* 영화 클릭 횟수 저장 위해 Movie 모델의  click_count 필드 추가
* 사용자가 클릭한 영화를 보여주기 위해 Movie와 User 간 M:N 관계를 설정
  * 사용자가 영화를 클릭하면 중개테이블에 user_id와 movie_id 저장



## D. 주요기능 / logic

![캡처333](https://user-images.githubusercontent.com/109324632/203733339-53f7d752-06aa-417f-a4eb-adda91cc52e6.PNG)

* Index 페이지 (GET 방식)

  * 로그인 안 되어 있으면 Signup, Login 보여줌
  * 로그인 후 
    * Genre, Era, Country 중 한 가지 선택하면 세부 Genre, Era, Country로 이동
    * Recommend, Profile, Logout 네비게이션 바 보여줌

* Genre, Era, Country 페이지 (GET 방식)

  * Genre 페이지

    * 장르별 영화개수 산정 후 많은 순서대로 글씨 사이즈 크게 출력

      ```python
      ## 장르별 영화개수 산정
      movies_counts = Genre.objects.annotate(Count("movies"))
      
      print(movies_counts) 
      # [장르, 영화개수]를 쿼리셋 형태로 가져옴 
      # <QuerySet [<Genre: Genre object (12)>, <Genre: Genre object (14)>, <Genre: Genre object (16)>, ...
      print(movies_counts[1].movies__count) 
      # Genre 14의 영화개수 출력
      ```

      ```python
      ## templates로 데이터 넘겨주기 (Word Cloud 출력하는 모든 페이지의 데이터 형태는 이와 같음)
      # AnyChart tool을 사용하기 위해 다음과 같은 형태로 넘겨줌
      # [{'x': action, 'value': 200}, {'x': romance, 'value': 100}, ...] 
      # value 값이 큰 x값을 가장 크게 출력
      results = []
      for q in movies_counts:
          specific_genre = Genre.objects.get(pk=q.pk)
          results.append(
              {
                  'x': specific_genre.name, # action
                  'value': q.movies__count # 200
              }
          )
      ```

  * Era 페이지

    * 시대별 영화개수 산정 후 많은 순서대로 글씨 사이즈 크게 출력

      ```python
      ## 년도별 영화개수 구하기
      years_countmovies = Movie.objects.annotate(year=TruncYear('released_date')).values('year').annotate(Count('movie_num'))
      # Trunc는 중요한 구성 요소까지 날짜를 자른다는 의미 / TruncYear은 년도까지만 자른다. 
      # ex) released_date가 2022-11-18이면 TruncYear('released_date')는 2022-01-01이 된다. 
      ```

      ```python
      ## 시대별로 묶어주기(조건문 사용)
      # 년도의 앞 세자리가 193일 때, 194일 때, ... 202일 때
      for year_countmovies in years_countmovies:
          if str(year_countmovies['year'].date())[0:3] == '193':
              era_1930 += year_countmovies['movie_num__count']
          elif str(year_countmovies['year'].date())[0:3] == '194':
              era_1940 += year_countmovies['movie_num__count']
      	...
      ```

  * Country 페이지

    * 국가별 영화개수 산정 후 많은 순서대로 글씨 사이즈 크게 출력

      ```python
      ## 국가별 영화개수 산정
      country_countmovies = Detail.objects.values('production_countries').annotate(Count('pk'))
      
      print(country_countmovies) 
      # <QuerySet [{'production_countries': 'Argentina', 'pk__count': 26}, {'production_countries': 'Australia', 'pk__count': 57}, ...
      ```

* 세부 Genre, Era, Country 페이지 (GET 방식, POST 방식)

  * 세부 Genre 페이지 (ex) action) (GET 방식)

    * 액션 장르의 영화 랜덤 20개 추출 후, (평점*관객수) 높은 순서대로 글씨 사이즈 크게 출력

      ```python
      ## 액션 장르의 영화 랜덤 20개 추출
      def category_genre_detail(request, genre_name): # genre_name을 인자값으로 받음
          genre = Genre.objects.get(name=genre_name) # 특정 genre 가져옴
          movies = genre.movies.all() # 특정 genre의 영화 모두 가져옴
          random_movies = random.choices(movies, k=20) # 랜덤 20개 추출
      ```

      ```python
      ## value 값에 (평점*관객수)를 넣어줌
      movies_dict = []
      for movie in random_movies:
          movies_dict.append(
              {
                  'x': movie.title,
                  'value' : movie.vote_avg*movie.vote_count
              }
          )
      ```

  * 세부 Era 페이지 (ex) 2020s) (GET 방식)

    * 2020년대 영화 랜덤 20개 추출 후, (평점*관객수) 높은 순서대로 글씨 사이즈 크게 출력

      ```python
      ## 2020년대 영화 랜덤 20개 추출
      def category_era_detail(request, era): # era(string 타입)을 인자값으로 받음
          era_number = int(era[0:4]) # '2020'를 int로 바꿈
          startdate = datetime.date(era_number, 1, 1) # 시작일 2020-01-01
          enddate = datetime.date(era_number+10, 1, 1) # 종료일 2030-01-01
          era_movies = Movie.objects.filter(released_date__range=[startdate, enddate]) # released_date가 시작일과 종료일 사이인 영화들을 필터링 
          random_movies = random.choices(era_movies, k=20) # 랜덤 20개 추출
      ```

  * 세부 Country 페이지 (ex) south korea) (GET 방식)

    * south korea 영화 랜덤 20개 추출, (평점*관객수) 높은 순서대로 글씨 사이즈 크게 출력

      ```python
      ## south korea 영화 랜덤 20개 추출
      def category_country_detail(request, country): # country를 인자값으로 받음
      	country_movies = Detail.objects.filter(production_countries=country) # production_countries가 south korea인 영화들을 필터링
      ```

  * 세부 Genre, Era, Country 페이지에서 영화 제목을 클릭하면

    * movie_click 함수를 거치고 (POST 방식!! 핵심기능!!)

      ```python
      def movie_click(request, movie_pk):
          if request.user.is_authenticated:
              movie = Movie.objects.get(pk=movie_pk)
              
              # 유저가 영화를 클릭하면 유저id-무비id 저장  
              request.user.click_movies.add(movie_pk)
              
              # 해당 영화의 click_count 필드 +1
              if movie.click_count:
                  movie.click_count += 1
              else:
                  movie.click_count = 1
              movie.save()
              return redirect('movies:movie_detail', movie_pk)
          return redirect('accounts:login')
      ```

    * Detail 페이지를 보여준다.

* Detail 페이지 (GET 방식)

  * 배경을 backdrop_path로 보여준다.
  * 영화 데이터 정보(title, genre, released date 등)를 Word Cloud로 출력
  * 왼쪽 상단에 로고를 넣어 index 페이지로 돌아가게 한다.

* Recommend 페이지 (GET 방식)

  * Movie 모델의 click_count가 높은 순서대로 10개 출력

    ```python
    movies_click10 = Movie.objects.order_by('-click_count')[:10]
    ```

* Profile 페이지 (GET 방식)

  * 내가 클릭한 영화 제목 출력

  * 영화의 장르들을 통계낸 후, 본인이 가장 좋아하는 장르 5순위를 도넛 차트로 보여줌

    ```python
    like_genres = [
        {'x':'Adventure', 'value':0},
        {'x':'Fantasy', 'value':0},
        {'x':'Animation', 'value':0},
        {'x':'Drama', 'value':0},
        ...
    ]
    
    ## 내가 클릭한 영화 제목 출력
    for movie in person.click_movies.all():
        movies_dict.append(
            {
                'x': movie.title,
                'value' : movie.vote_avg*movie.vote_count
            }
        )
        
    	## 영화의 장르들을 통계낸 후, 본인이 가장 좋아하는 장르 5순위를 도넛 차트로 보여줌
    	for genre in movie.genres.all(): # 영화의 장르들을 하나씩 뽑아내어 
            for like_genre in like_genres: # like_genres의 'x'와 같으면 'value'값 +1 해주기
                if genre.name == like_genre['x']:
                    like_genre['value'] += 1
                    
    like_genres = sorted(like_genres , key= lambda x: x['value'], reverse=True) 
    # like_genres 리스트를 value 값이 큰 순서대로 sort
    ```

  

## E. 기대 효과

* 현대인의 고질병. 결정 장애 해결 도움
* 직관적이고 간편한 정보 제공 통해 서비스 이용 접근성 증가
* 참여형 서비스(개인의 선택이 또 다른 개인의 선택에 영향) 제공 통해 사용자들의 흥미 유발



## F. 후기

* 노영찬 : 즐거웠습니다 : D
* 정유현 : 
