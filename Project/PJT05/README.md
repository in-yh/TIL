# PJT 05

### 이번 pjt 를 통해 배운 내용

- DB를 활용한 웹 페이지 구현
- 데이터 생성, 조회, 수정, 삭제하는 기본 Web 제작
- Django ModelForm을 활용한 사용자 요청 데이터 유효성 검증



## A. base.html

- 요구 사항 :

  * 공통 부모 템플릿 만들기

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * base.html에 navbar 추가 시도
  
  ```python
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      .fantasy { font-family: fantasy; }
      .ser { font-family: Georgia, "맑은 고딕", serif; }
    </style>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  </head>
  <body>
    <nav class="navbar navbar-light bg-light m-0 p-0">
      <div class="container-fluid d-flex justify-content-between bg-body">
        <a class="navbar-brand fantasy m-0" href="{% url 'movies:index' %}"> 
          My Movies
        </a>
        <a href="">CREATE</a>
      </div>
    </nav>
  
    <div class="container">
      <div class="row ser">
        {% block content %}
        {% endblock content %}
      </div>
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
  </html>
  ```
  
  - 이 문제에서 어려웠던 점
    * navbar를 만들어보고자 했으나, 제목을 가운데 create를 오른쪽에 정렬 하는 법을 잘 모르겠어서 양 사이드로 정렬함..
  - 내가 생각하는 이 문제의 포인트
    * d-flex와 grid 재공부 필요..

------

 

## B. index.html

- 요구 사항 :

  * 전체 영화 목록 조회 페이지

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 데이터베이스에 존재하는 모든 영화의 목록 표시 (영화 제목 및 평점을 표시)
    * 영화 제목 클릭 시 해당 영화의 상세 조회 페이지(detail.html)로 이동

  ```python
  # movies/models.py
  from django.db import models
  
  class Movie(models.Model):
      title = models.CharField(max_length=20)
      audience = models.IntegerField()
      release_date = models.DateField()
      genre = models.CharField(max_length=30)
      score = models.FloatField()
      poster_url = models.TextField()
      description = models.TextField()
  
  # movies/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'movies'
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  
  # movies/views.py
  from django.shortcuts import render, redirect
  from django.views.decorators.http import require_safe, require_POST, require_http_methods
  from .models import Movie 
  
  @require_safe
  def index(request):
      movies = Movie.objects.all() # 데이터베이스에 있는 movie정보를 모두 가져옴
      context = {
          'movies': movies,
      }    
      return render(request, 'movies/index.html', context) 
  ```
  
  ```html
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>INDEX</h1>
    <a href="{% url 'movies:create' %}">CREATE</a> 
    <hr>
    {% for movie in movies %}
      <p><a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></p> 
      <p>{{ movie.score }}</p>
      <hr>
    {% endfor %}
  
  {% endblock content %}
  ```
  
  - 이 문제에서 어려웠던 점
    * 특별한 건 없었음.
    
  - 내가 생각하는 이 문제의 포인트 
  
    * 데이터베이스에 있는 movie정보를 모두 가져온 후 index.html에서 for문 사용하여 한 개씩 추출해줌
    * movie title을 클릭하면 detail페이지로 갈 수 있게 a 태그 달아줌
  
    * GET 방식만 허용된다기에 데코레이터 넣어줌(@require_safe)

------

 

## C. detail.html

* 요구 사항: 
  * 영화 상세 정보 페이지

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 특정 영화의 상세 정보 표시
    * Bootstrap Card Component 사용
    * 해당 영화의 수정 및 삭제 버튼 표시
    * 뒤로가기로 index.html로 이동하는 링크 표시
  
  ```python
  # movies/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'movies'
  urlpatterns = [
      path('<int:pk>/', views.detail, name='detail'),
      path('<int:pk>/delete/', views.delete, name='delete'),
  ]
  
  # movies/views.py
  from django.shortcuts import render, redirect
  from django.views.decorators.http import require_safe, require_POST, require_http_methods
  from .models import Movie 
  
  @require_safe
  def detail(request, pk):
      movie = Movie.objects.get(pk=pk)
      context = {
          'movie': movie,
      }
      return render(request, 'movies/detail.html', context)
  
  @require_POST
  def delete(request, pk):
      movie = Movie.objects.get(pk=pk)
      movie.delete()
      return redirect('movies:index')
  ```
  
  ```html
  {% extends 'base.html' %}
  {% load bootstrap5 %}
  
  {% block content %}
    <h1 class="d-flex justify-content-center">Detail</h1>
    <hr>
    {% comment %} 가운데 정렬 위해 카드를 div태그 안에 넣어줌 {% endcomment %}
    <div class="d-flex justify-content-center"> 
      <div class="card" style="width: 20rem;">
        <img src="{{ movie.poster_url }}" class="card-img-top" alt="no_image">
        <div class="card-body">
          <h5 class="card-title">{{ movie.title }}</h5>
          <p class="card-text">Audience : {{ movie.audience }}</p>
          <p class="card-text">Realese Dates : {{ movie.release_date }}</p>
          <p class="card-text">Genre : {{ movie.genre }}</p>
          <p class="card-text">Score : {{ movie.score }}</p>
          <p class="card-text">{{ movie.description }}</p>
          <div class="d-flex">
            <div class="me-2">
              <a href="{% url 'movies:update' movie.pk %}"> 
                <input type="submit" value="UPDATE" class="btn btn-info">
              </a>
            </div>
            <div class="mx-2">
              <form action="{% url 'movies:delete' movie.pk %}" method="POST">
                {% csrf_token %}
                <input type="submit" value="DELETE" class="btn btn-danger">
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
    {% comment %} a 태그 안에 input이든 button이든 넣어줘야 작은 박스로 처리할 수 있음 이거 안하면 길게 한 줄로 늘어짐 {% endcomment %}
    <a href="{% url 'movies:index' %}"> 
      <button type="submit" class="btn btn-warning">BACK</button>
      {% comment %} <input type="submit" value="BACK" class="btn btn-warning">  {% endcomment %}
    </a>
  {% endblock content %}
  ```
  
  - 이 문제에서 어려웠던 점
    * detail 글씨와 card 가운데 정렬하는 법
  - 내가 생각하는 이 문제의 포인트 
    * detail 글씨는 h1태그에 넣어주고, card는 상위에 div태그를 넣어줘서 정렬함
    * a태그는 inline이 아닌 block 형태이기 때문에 아래 button 혹은 input태그를 넣어줘야 길게 늘어지지 않고 버튼처럼 사용할 수 있음 

------

 

## D. create.html

* 요구 사항: 
  * 영화 생성 페이지

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 특정 영화를 생성하기 위한 form 작성
    * 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm
    * 작성한 정보는 제출(submit) 시 단일 영화 데이터를 저장하는 URL로 요청과 함께 전송
    * 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크 표시
  
  ```python
  # movies/forms.py
  from django import forms
  from .models import Movie
  
  class MovieForm(forms.ModelForm):
      # 위젯 설정
      # 장르
      A = 'comedy'
      B = 'horror'
      C = 'romance'
      GENRE_CHOICES = [
          (A, '코미디'),
          (B, '공포'),
          (C, '로맨스'),
      ]
      genre = forms.ChoiceField(choices=GENRE_CHOICES)
  
      # 스코어
      score = forms.FloatField( # django/forms/fields에서 있는지 확인
          widget=forms.NumberInput( # django/forms/widget에서 있는지 확인
              attrs={
                  'step' : 0.5,
                  'min' : 0,
                  'max' : 5,
              }
          )
      )
  
      # 개봉일
      release_date = forms.DateField( 
          widget=forms.DateInput(
              attrs={
                  'type' : 'date',
              }
          )
      )
      
      class Meta:
          model = Movie
          fields = '__all__'
  
  # movies/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'movies'
  urlpatterns = [
      path('create/', views.create, name='create'),
  ]
  
  # movies/views.py
  from django.shortcuts import render, redirect
  from django.views.decorators.http import require_safe, require_POST, require_http_methods
  from .models import Movie 
  from .forms import MovieForm
  
  @require_http_methods(['GET', 'POST'])
  def create(request):
      if request.method == 'POST':
          form = MovieForm(request.POST)
          if form.is_valid():
              movie = form.save() # 자기자신으로 반환
              return redirect('movies:detail', movie.pk)
      else:
          form = MovieForm()
      context = {
          'form': form,
      }
      return render(request, 'movies/create.html', context)
  ```
  
  ```html
  {% extends 'base.html' %}
  {% load bootstrap5 %} 
  {% comment %} bootstrap5 설치, 등록, 로드&사용법 숙지하기! {% endcomment %}
  
  {% block content %}
    <h1>CREATE</h1>
    <form action="{% url 'movies:create' %}" method="POST"> 
      {% csrf_token %}
      {% bootstrap_form form %}
      {% buttons %}
        <button type="submit" class="btn btn-primary">Submit</button>
      {% endbuttons %}
    </form>
    <hr>
    <a href="{% url 'movies:index' %}"> 
      {% buttons %}
        <button type="submit" class="btn btn-info">BACK</button>
      {% endbuttons %}
    </a>
  {% endblock content %}
  ```
  
  - 이 문제에서 어려웠던 점
    * 위젯 설정하려고 공식문서도 보고 장고 깃허브도 보았는데 attrs에 어떤 값을 넣을 수 있는지 아직 제대로 찾지 못했다.
    * bootstrap5 사용하는 법 생소
  - 내가 생각하는 이 문제의 포인트 
    * django/forms/fields에서 폼필드 확인 및 django/forms/widget에서 input 요소 확인
    * bootstrap5 설치, 등록, 사용법 재숙지함
      * 설치 : bash에서 pip install django-bootstrap-v5
      * 등록 : INSTALLED_APPS에서 'bootstrap5', 추가
      * 사용법
        * load : {% load bootstrap5 %}
        * form : {% bootstrap_form form %}

------

 

## E. update.html

* 요구 사항: 
  * 영화 수정 페이지

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 특정 영화 수정하기 위한 form 작성
    * 표시되는 form은 Movie 모델 클래스에 기반한 ModelForm
    * input 요소에는 기존 데이터 출력
    * Cancel 버튼은 사용자의 모든 입력을 초기 값으로 재설정
    * 작성한 정보는 제출(submit) 시 단일 영화 데이터를 수정하는 URL로 요청과 함께 전송
    * detail.html로 이동하는 링크 표시
  
  ```python
  # movies/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'movies'
  urlpatterns = [
      path('<int:pk>/update/', views.update, name='update'),
  ]
  
  # movies/views.py
  from django.shortcuts import render, redirect
  from django.views.decorators.http import require_safe, require_POST, require_http_methods
  from .models import Movie 
  from .forms import MovieForm
  
  @require_http_methods(['GET', 'POST'])
  def update(request, pk):
      movie = Movie.objects.get(pk=pk)
      if request.method == 'POST':
          form = MovieForm(request.POST, instance=movie)
          if form.is_valid():
              form.save()
              return redirect('movies:detail', movie.pk)
      else:
          form = MovieForm(instance=movie)
      context = {
          'form': form,
          'movie': movie, # 이거 안해주면.. url 쓸 때 movie.pk가 작동 안 됨..
      }
      return render(request, 'movies/update.html', context)
  ```
  
  ```html
  {% extends 'base.html' %}
  {% load bootstrap5 %}
  
  {% block content %}
    <h1>UPDATE</h1>
    <hr>
    <form action="{% url 'movies:update' movie.pk %}" method="POST"> 
      {% csrf_token %}
      {% bootstrap_form form %}
      {% buttons %} {% comment %} 이 태그는 쓰나 안쓰나 보여지는 건 똑같음 {% endcomment %}
        <button type="submit" class="btn btn-primary">Submit</button>
        <button type="reset" class="btn btn-primary">Cancel</button> {% comment %} type을 reset으로! {% endcomment %}
      {% endbuttons %}
    </form>
    <hr>
    {% comment %} a 태그 안에 input이든 button이든 넣어줘야 작은 박스로 처리할 수 있음 이거 안하면 길게 한 줄로 늘어짐 {% endcomment %}
    <a href="{% url 'movies:detail' movie.pk %}">
      <button type="submit" class="btn btn-info">BACK</button> 
    </a>
  {% endblock content %}
  ```
  
  - 이 문제에서 어려웠던 점
    * update GET 방식에서 movie도 context에 넣어줘야 하는데, 그러지 않아서 update.html에서 url 부분에서 movie를 찾을 때 오류가 발생하였다.
  - 내가 생각하는 이 문제의 포인트 
    * html에서 변수 사용할 때, context 잘 확인하기

------



# 후기

- 저번에 공부했던 부분이라 조금은 수월하게 작성했던 것 같다.
- 다만, CSS부분을 좀 더 욕심내서 하려 했으나.. 배열하는 부분이 역시나 힘들었다. d-flex와 grid를 다시 공부해봐야겠다 생각했음!
- 이후 인증 부분과 댓글 작성하는 법(N:1)도 이번주 안으로 재공부해야지..