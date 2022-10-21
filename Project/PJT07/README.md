# PJT 07

### 이번 pjt 를 통해 배운 내용

- DB 설계를 활용한 REST API 설계

- DRF(Django Rest Framework)를 활용한 API Server 제작

- 1:N , M:N에 대한 이해

  

## A. 전체 배우 목록 제공

- 결과 : 

  - 문제 접근 방법 및 코드 설명

  ```python
  # models.py
  from django.db import models
  
  class Actor(models.Model):
      name = models.CharField(max_length=100)
  
      
  # serializers.py
  from rest_framework import serializers
  from .models import Actor
  
  class ActorListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Actor
          fields = '__all__'
  
          
  # urls.py
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('actors/', views.actor_list),
  ]
  
  
  # views.py
  from rest_framework.response import Response # response에서 가져오는거
  from rest_framework.decorators import api_view # api는 무조건 api_view가 있어야 함!!
  from .models import Actor
  from .serializers import ActorListSerializer
  
  @api_view(['GET'])
  def actor_list(request):
      actors = Actor.objects.all()
      serializer = ActorListSerializer(actors, many=True) # serializer를 할 데이터를 넣어주고, 쿼리셋 형태라면 many=True 추가
      return Response(serializer.data) # 응답은 Response로 하기
  ```

  - 이 문제에서 어려웠던 점
    * api_view를 자꾸 까먹어서.. 에러 발생..
  - 내가 생각하는 이 문제의 포인트
    * 정보를 모두 받은 다음, serializer로 묶어준 후 data 보여준다.

------

 

## B. 단일 배우 정보 제공(출연 영화 제목 포함)

- 결과 : 

  - 문제 접근 방법 및 코드 설명

  ```python
  # models.py
  class Actor(models.Model):
      name = models.CharField(max_length=100)
  
      
  class Movie(models.Model):
      title = models.CharField(max_length=100)
      overview = models.TextField()
      release_date = models.DateTimeField()
      poster_path = models.TextField()
      actors = models.ManyToManyField(Actor, related_name='movies') # movies_movie_actors 테이블 생김 
  
      
  # serializers.py
  from .models import Actor, Movie
   
  class MovieTitleSerializer(serializers.ModelSerializer): # Movie에서 제목만 출력
  
      class Meta:
          model = Movie
          fields = ('title',)
  
          
  class ActorSerializer(serializers.ModelSerializer): # 특정 Actor가 출연한 Movie 목록 조회하기 (역참조)
  
      movies = MovieTitleSerializer(many=True, read_only=True) # 제목만 출력되게 함
  
      class Meta:
          model = Actor
          fields = '__all__'
  
          
  # urls.py
  urlpatterns = [
      path('actors/', views.actor_list),
      path('movies/', views.movie_list),
      path('reviews/', views.review_list),
      path('actors/<int:actor_pk>/', views.actor_detail),
  ]
  
  
  # views.py
  from .serializers import ActorListSerializer, MovieListSerializer, ReviewListSerializer, ActorSerializer
      
  @api_view(['GET'])
  def actor_detail(request, actor_pk):
      actor = Actor.objects.get(pk=actor_pk)
      serializer = ActorSerializer(actor) # 하나면 그냥 객체만 넣어줌
      return Response(serializer.data)
  ```

  - 이 문제에서 어려웠던 점
    * M:N으로 묶여있는 필드들을 serializer 만들 때 어떻게 작성할 수 있는지

  - 내가 생각하는 이 문제의 포인트 

    * 특정 Actor가 출연한 Movie 목록 조회해야 하는데, Actor 모델의 필드에는 movie에 대한 필드가 없다.
    * 그렇기에 Actor와 Movie가 M:N으로 묶여있기에 중개 테이블을 활용할 수 있다.
    * Actor에서 Movie 목록을 가져와야 하므로 즉, Actor가 1, Movie가 N이기 때문에 Actor에서 Movie를 역참조 해야 한다.
    * 역참조할 때 related name이 'movies'로 정해져 있으므로 ActorSerializer 내에 movies를 정의해준다.
    * 우리가 영화 정보로 필요한 것은 제목이므로 제목만 출력하는 Serializer(MovieTitleSerializer)를 새로 생성한다.
    * MovieTitleSerializer를 movies 정의할 때 사용해주면 제목만 serializer를 해주게 된다.

------

 

## C. 전체 영화 목록 제공

- 결과 : 

  - 문제 접근 방법 및 코드 설명
  
  ```python
  # models.py
  class Movie(models.Model):
      title = models.CharField(max_length=100)
      overview = models.TextField()
      release_date = models.DateTimeField()
      poster_path = models.TextField()
      actors = models.ManyToManyField(Actor, related_name='movies') # movies_movie_actors 테이블 생김 
  
      
  # serializers.py
  from .models import Actor, Movie
  
  class MovieListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Movie
          fields = ('title', 'overview',)
  
          
  # urls.py
  urlpatterns = [
      path('actors/', views.actor_list),
      path('movies/', views.movie_list),
  ]
  
  
  # views.py
  from .models import Actor, Movie
  from .serializers import ActorListSerializer, MovieListSerializer
  
  @api_view(['GET'])
  def movie_list(request):
      movies = Movie.objects.all()
      serializer = MovieListSerializer(movies, many=True)
      return Response(serializer.data)
  ```
  
  - 이 문제에서 어려웠던 점
    * A와 똑같이 생각하면 큰 어려움 없음
  - 내가 생각하는 이 문제의 포인트 
    * Movie와 Actor를 M:N으로 생각하여 새로운 중개 테이블 생성하기

------

 

## D. 단일 영화 정보 제공(출연 배우 이름과 리뷰 목록 포함)

- 결과 : 

  - 문제 접근 방법 및 코드 설명
  
  ```python
  # models.py
  class Actor(models.Model):
      name = models.CharField(max_length=100)
      # movies = models.ManyToManyField(Movie, related_name='actors') # 이러면 Movie 모델 먼저 써줘야해
  
  
  class Movie(models.Model):
      title = models.CharField(max_length=100)
      overview = models.TextField()
      release_date = models.DateTimeField()
      poster_path = models.TextField()
      actors = models.ManyToManyField(Actor, related_name='movies') # movies_movie_actors 테이블 생김 
  
  
  class Review(models.Model):
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
      title = models.CharField(max_length=100)
      content = models.TextField()
  
      
  # serializers.py
  from .models import Actor, Movie, Review
  
  class ActorNameSerializer(serializers.ModelSerializer): # Actor에서 name만 출력하게 함 / 이렇게 하나하나 만드는게 맞나?
  
      class Meta:
          model = Actor
          fields = ('name',)
  
  
  class MovieSerializer(serializers.ModelSerializer): # 특정 Movie의 정보 제공
  
      actors = ActorNameSerializer(many=True, read_only=True)
      review_set = ReviewListSerializer(many=True, read_only=True) # 역참조
  
      class Meta:
          model = Movie
          fields = '__all__'
          # 위의 actors를 정의해주기 전에는 여기서 '__all__'을 해주면 actors의 번호가 들어감
          # 그래서 exclude = ('actors',)를 해서 제거를 해주고 위에 actors를 정의해줬는데 에러발생
          # '__all__'을 해주고 위에 actors 정의해주면 번호였던 것이 알아서 내용이 들어감
  
          
  # urls.py
  urlpatterns = [
      path('actors/', views.actor_list),
      path('movies/', views.movie_list),
      path('reviews/', views.review_list),
      path('actors/<int:actor_pk>/', views.actor_detail),
      path('movies/<int:movie_pk>/', views.movie_detail),
  ]
  
  
  # views.py
  from .serializers import ActorListSerializer, MovieListSerializer, ReviewListSerializer, ActorSerializer, MovieSerializer
  
  @api_view(['GET'])
  def movie_detail(request, movie_pk):
      movie = Movie.objects.get(pk=movie_pk)
      serializer = MovieSerializer(movie) # 하나면 그냥 객체만 넣어줌
      return Response(serializer.data)
  ```
  
  - 이 문제에서 어려웠던 점
    * 특정 Movie 정보를 제공하는 MovieSerializer 작성하는 것(출연 배우 이름과 리뷰 목록 보여주기)
    * Actor에서 name만 출력하게 해주는 Serializer 또 만듦.. 새로 만들지 않고 원래 있던 Serializer에서 필요한 필드만 추출할 수는 없을까?
  - 내가 생각하는 이 문제의 포인트 
    * 출연 배우 이름 보여주기
      * Movie(1)에서 Actor(N)를  actors라는 manager로 참조한다.
      * Meta 내 `exclude = ('actors',)`를 해주면 위에 정의한 actors를 출력할 수 없게 되므로 에러 발생
    * 리뷰 목록 보여주기
      * Movie(1)에서 Review(N)를 review_set이라는 manager로 역참조한다.

------

 

## E. 전체 리뷰 목록 제공

- 결과 : 

  - 문제 접근 방법 및 코드 설명
  
  ```python
  # models.py
  class Review(models.Model):
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
      title = models.CharField(max_length=100)
      content = models.TextField()
  
      
  # serializers.py
  from .models import Actor, Movie, Review
  
  class ReviewListSerializer(serializers.ModelSerializer):
  
      class Meta:
          model = Review
          fields = ('title', 'content',)
  
          
  # urls.py
  urlpatterns = [
      path('actors/', views.actor_list),
      path('movies/', views.movie_list),
      path('reviews/', views.review_list),
  ]
  
  
  # views.py
  from .models import Actor, Movie, Review
  from .serializers import ActorListSerializer, MovieListSerializer, ReviewListSerializer
  
  @api_view(['GET'])
  def review_list(request):
      reviews = Review.objects.all()
      serializer = ReviewListSerializer(reviews, many=True)
      return Response(serializer.data)
  ```
  
  - 이 문제에서 어려웠던 점
    * A, C와 동일해서 어려운 점 없었음
  - 내가 생각하는 이 문제의 포인트 
    * Movie와 Review를 1:N관계로 만듦

------



## F. 단일 리뷰 조회 & 수정 & 삭제

- 결과 : 

  - 문제 접근 방법 및 코드 설명

  ```python
  # models.py
  class Review(models.Model):
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
      title = models.CharField(max_length=100)
      content = models.TextField()
  
      
  # serializers.py
  class ReviewSerializer(serializers.ModelSerializer):
  
      movie = MovieTitleSerializer(read_only=True) # 참조, 1개를 가져오기에 many=True는 하지 않는다.
  
      class Meta:
          model = Review
          fields = '__all__'
          
          
  # urls.py
  urlpatterns = [
      path('actors/', views.actor_list),
      path('movies/', views.movie_list),
      path('reviews/', views.review_list),
      path('actors/<int:actor_pk>/', views.actor_detail),
      path('movies/<int:movie_pk>/', views.movie_detail),
      path('reviews/<int:review_pk>/', views.review_detail),
  ]
  
  
  # views.py
  from rest_framework import status
  from .serializers import ActorListSerializer, MovieListSerializer, ReviewListSerializer, ActorSerializer, MovieSerializer, ReviewSerializer
  
  @api_view(['GET', 'PUT', 'DELETE'])
  def review_detail(request, review_pk):
      review = Review.objects.get(pk=review_pk)
      if request.method == 'GET':
          serializer = ReviewSerializer(review)
          return Response(serializer.data)
      
      elif request.method == 'PUT':
          serializer = ReviewSerializer(review, data=request.data) # 인스턴스가 앞쪽으로 들어감
          if serializer.is_valid(raise_exception=True): # 유효성 검증 통과하지 못하면 400에러 뜨게 함
              serializer.save()
              return Response(serializer.data) # 200이라서 별도 뭐 없음
  
      elif request.method == 'DELETE':
          review.delete() # 삭제는 그냥 삭제, serializer 할 것도 없지
          return Response({ 
              "delete" : f'review {review_pk} is deleted'
          }, status = status.HTTP_204_NO_CONTENT)
          # delete 화면 만들어주기
  ```

  - 이 문제에서 어려웠던 점
    * `@api_views()`를 자꾸 까먹어서 에러 발생
    * PUT일 때 
      * 이전 데이터를 넣어줘야 하는데 인스턴스를 앞쪽으로 넣어줘야 함
      * 유효성 검증할 때 통과하지 못하면 400에러 뜨게 하는 것으로 `raise_exception=True` 넣어 줌(예외를 떠오르게 한다.)
    * DELETE일 때
      * 삭제 후 메세지 출력 위해 Response 안에 딕셔너리 형태로 넣어주고 변수값 출력 위해 f-string 사용 
    * Review(1) 내 Movie(1)의 title 정보도 출력하기 위해 movie라는 manager를 사용(참조)하여 새로운 Serializer(ReviewSerializer)를 만든다. 이 때, Movie(1)는 1개이기 때문에 many=True는 하지 않는다.
  - 내가 생각하는 이 문제의 포인트 
    * Review(1) 내 Movie(1)의 title 정보도 출력하기 위해 movie라는 manager를 사용(참조)하여 새로운 Serializer(ReviewSerializer)를 만드는 것

------



## G. 리뷰 생성

- 결과 : 

  - 문제 접근 방법 및 코드 설명

  ```python
  # models.py
  class Review(models.Model):
      movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
      title = models.CharField(max_length=100)
      content = models.TextField()
      
      
  # serializers.py
  class ReviewSerializer(serializers.ModelSerializer):
  
      movie = MovieTitleSerializer(read_only=True) # 참조, 1개를 가져오기에 many=True는 하지 않는다.
  
      class Meta:
          model = Review
          fields = '__all__'
          
          
  # urls.py
  urlpatterns = [
      path('actors/', views.actor_list),
      path('movies/', views.movie_list),
      path('reviews/', views.review_list),
      path('actors/<int:actor_pk>/', views.actor_detail),
      path('movies/<int:movie_pk>/', views.movie_detail),
      path('reviews/<int:review_pk>/', views.review_detail),
      path('movies/<int:movie_pk>/reviews/', views.create_review)
  ]
  
  
  # views.py
  @api_view(['POST'])
  def create_review(request, movie_pk):
      movie = Movie.objects.get(pk=movie_pk)
      serializer = ReviewSerializer(data=request.data) # 내가 넣은 데이터를 가져오고(그냥 조회만 한다면 조회할 객체를 넣어주면 돼)
      if serializer.is_valid(raise_exception=True): # 그 데이터가 유효하다면
          serializer.save(movie=movie) # 저장하는데, movie 정보는 읽기 전용 필드이므로 여기서 넣어줘
          return Response(serializer.data, status=status.HTTP_201_CREATED)
  ```

  - 이 문제에서 어려웠던 점
    * ReviewSerializer에 생성할 data를 넣어준다. (그냥 조회만 한다면 조회할 객체를 넣어주면 되지만)
    * movie는 읽기 전용 필드이므로 (data 정보에는 movie_id 정보는 포함되지 않으므로 즉, 생성하는 사람이 넣어주는 것이 아니므로) save할 때 movie정보를 views.py에서 지정해준다(객체를 넣어줌. 이전 N:1 M:N 모델에서 commit=False 넣어 객체로 받아준 것처럼)
  - 내가 생각하는 이 문제의 포인트 
    * movie는 읽기 전용 필드이므로 views.py에서 지정해줘야 함

------



# 후기

- 교재, 필기 없이 혼자 해보라고 하면 완벽히 짤 수 있을까..
- 근데 templates을 안 짜도 되기 때문에 그건 또 편한 듯하다

