# PJT 04

### 이번 pjt 를 통해 배운 내용

- 데이터 생성, 조회, 수정, 삭제하는 기본 Web 제작
- url, view, template 순으로 작성 및 Django Model 활용



## A. base.html

- 요구 사항 :

  * 공통 부모 템플릿 만들기 (모든 템플릿 파일은 base.html을 상속받아 사용)

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 최상위 폴더 안에 templates 폴더 만들고 그 안에 base.html 만들기
    * 프로젝트 폴더 내 settings.py에 적어주기

  ```python
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  </head>
  <body>
      
      <div class="container">
          <div class="row">
              {% block content %}
              {% endblock content %}
          </div>
      </div>
  
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  - 이 문제에서 어려웠던 점
    * 특별한 건 없었음. 
  - 내가 생각하는 이 문제의 포인트
    * settings.py 파일에 잊지 말고 추가해주기

------

 

## B. inedx.html

- 요구 사항 :

  * 전체 영화 목록 조회 페이지

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 데이터베이스에 존재하는 모든 영화의 목록 표시 (영화 제목 및 평점을 표시)
    * 영화 제목 클릭 시 해당 영화의 상세 조회 페이지(detail.html)로 이동

  ```python
  # movies/urls.py
  from django.urls import path
  from . import views 
  
  app_name = 'movies'
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  
  # movies/views.py
  from django.shortcuts import render
  from .models import Movie
  
  def index(request): 
      movies = Movie.objects.all() # 모든 영화 조회
      context = {
          'movies' : movies
      } # movies/index.html에 {{  }} 쓰이므로 여기서 정의 내려줘야 함.
      return render(request, 'movies/index.html', context)
  ```

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
      <h1 class="fw-bold">INDEX</h1> <!-- fontweight는 class에 담아서 작성(부트스트랩 이용) -->
      <a href="{% url 'movies:new' %}">[NEW]</a> <!-- NEW페이지로 이동할 링크 -->
      <hr>
      {% for movie in movies %} <!-- 전체를 가져오기에 하나씩 보여주려면 for문 돌려줘야 함 -->
          <p><a href="{% url 'movies:detail' movie.pk %}">{{movie.title}}</a></p> <!-- 영화 제목 클릭 시 detail.html로 이동, 이 때 detail은 pk라는 인자값이 필요하기에 뒤에 꼭 인자 붙여줘야 함. -->
          <p>{{movie.score}}</p>
          <hr>
      {% endfor %}
  {% endblock content %}
  ```

  - 이 문제에서 어려웠던 점
    * 특별한 건 없었음.
  - 내가 생각하는 이 문제의 포인트 
    * 영화 제목 클릭 시 detail.html로 이동하는 기능 구현 시, 하이퍼링크 주소를 movies:detail 로 하고 detail은 pk라는 인자값이 필요하므로 뒤에 인자를 붙여주는게 핵심!

------

 

## C. detail.html

* 요구 사항: 
  * 영화 상세 정보 페이지

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 특정 영화의 상세 정보 표시
    * 해당 영화의 수정 및 삭제 버튼 표시
    * 뒤로가기로 index.html로 이동하는 링크 표시

  ```python
  # movies/urls.py
  from django.urls import path
  from . import views 
  
  app_name = 'movies'
  urlpatterns = [
      path('', views.index, name='index'),
      path('<int:pk>/', views.detail, name='detail'), # 각각의 영화마다 페이지가 필요하므로 뒤에 pk값을 붙임
  ]
  
  # movies/views.py
  from django.shortcuts import render
  from .models import Movie
  
  def index(request):
      movies = Movie.objects.all() # 모든 영화 조회
      context = {
          'movies' : movies
      } # movies/index.html에 {{  }} 쓰이므로 여기서 정의 내려줘야 함.
      return render(request, 'movies/index.html', context)
  
  def detail(request, pk):
      movie = Movie.objects.get(pk=pk) # 특정 pk값이 들어오면 그 pk를 가진 레코드를 movie에 넣기
      context = {
          'movie' : movie
      }
      return render(request, 'movies/detail.html', context)
  '''
  .
  .
  .
  '''
  # 가장 마지막에 짬
  def delete(request, pk):
      movie = Movie.objects.get(pk=pk) # 그 행 가져온 다음
      movie.delete() # 삭제
      return redirect('movies:index')
  ```

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
      <h1 class="fw-bold">DETAIL</h1>
      <hr>
      <div class="card p-0" style="width: 18rem;"> <!-- 이미지를 카드에 넣어봄, padding이 있길래 0으로 바꿔서 카드 안에 꽉 차게 만듦 -->
          <img src="{{movie.poster_url}}" class="card-img-top" alt="no_image">    
      </div>
      <p class="fw-bold">{{movie.title}}</p> <!-- .title과 같이 데이터베이스에 접근할 때는 점+필드로 접근 -->
      <p>Audience : {{movie.audience}}</p>
      <p>Release Date : {{movie.release_date}}</p>
      <p>Genre : {{movie.genre}}</p>
      <p>Score : {{movie.score}}</p>
      <p>{{movie.description}}</p>
      <a href="{% url 'movies:edit' movie.pk %}">EDIT</a> <!-- EDIT링크 클릭시 edit으로 가게끔 함 -->
      <form action="{% url 'movies:delete' movie.pk %}" method="POST"> <!-- DELETE 버튼 클릭 시 삭제 시킴 -->
          {% csrf_token %}
          <input type="submit" value="DELETE">
      </form>
      <a href="{% url 'movies:index' %}">Back</a> <!-- 뒤로가기로 index.html로 이동하는 링크 표시 -->
  {% endblock content %}
  ```

  - 이 문제에서 어려웠던 점
    * EDIT랑 DELETE의 다른 점 (누르면 같이 동작하는 건 똑같은데, 왜 하나는 url로 보내주고 하나는 왜 form으로 가는건지..)
  - 내가 생각하는 이 문제의 포인트 
    * edit은 html이 있어서 거기서 form 작업함.
    * delete는 삭제만 해주고 끝나기 때문에 별도의 html 필요 없고 detail.html에서 form 작업

------

 

## D. new.html

* 요구 사항: 
  * 영화 생성 페이지

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 특정 영화를 생성하기 위한 form 작성
    * 작성한 정보는 제출(submit) 시 단일 영화 데이터를 저장하는 URL로 요청과 함께 전송
    * 전체 영화 목록 조회 페이지(index.html)로 이동하는 링크 표시

  ```python
  # movies/urls.py
  from django.urls import path
  from . import views 
  
  app_name = 'movies'
  urlpatterns = [
      path('', views.index, name='index'),
      path('<int:pk>/', views.detail, name='detail'), # 각각의 영화마다 페이지가 필요하므로 뒤에 pk값을 붙임
      path('new/', views.new, name='new'),
      path('create/', views.create, name='create'),
  ]
  
  # movies/views.py
  from django.shortcuts import render, redirect
  from .models import Movie
  
  def index(request):
      movies = Movie.objects.all() # 모든 영화 조회
      context = {
          'movies' : movies
      } # movies/index.html에 {{  }} 쓰이므로 여기서 정의 내려줘야 함.
      return render(request, 'movies/index.html', context)
  
  def detail(request, pk):
      movie = Movie.objects.get(pk=pk) # 특정 pk값이 들어오면 그 pk를 가진 레코드를 movie에 넣기
      context = {
          'movie' : movie
      }
      return render(request, 'movies/detail.html', context)
  
  def new(request):
      return render(request, 'movies/new.html')
  
  def create(request):
      title = request.POST.get('title') # POST로 받은 정보들을 각각 변수에 저장, 괄호 안의 값은 form 태그 안의 name 값을 적어줘야 함(따옴표 주의)
      audience = request.POST.get('audience')
      release_date = request.POST.get('release_date')
      genre = request.POST.get('genre')
      score = request.POST.get('score')
      poster_url = request.POST.get('poster_url')
      description = request.POST.get('description')
  
      # movie라는 인스턴스 생성하면서 받은 값을 필드에 맞춰 작성 & 저장
      movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
      movie.save()
      return redirect('movies:index') # 저장 끝나면 index창으로 감. redirect 이용
  ```

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
      <h1 class="fw-bold">NEW</h1>
      <hr>
      <form action="{% url 'movies:create' %}" method="POST"> <!-- 작성하고 submit 누르면 create로 전송됨 -->
          {% csrf_token %} <!-- POST 방식이므로 반드시 작성!! -->
          <label for="title">TITLE</label>
          <input type="text" id="title" name="title"><br>
          <label for="audience">AUDIENCE</label>
          <input type="text" id="audience" name="audience"><br>
          <label for="release_date">RELEASE_DATE</label>
          <input type="date" id="release_date" name="release_date"><br> <!-- input type 중에 date가 딱 있더라.. good! -->
          <label for="genre">GENRE</label>
          <select id="genre" name="genre"> <!-- select가 있네 -->
              <option value="코미디">코미디</option> <!-- value값으로 database에 저장되니 잘 설정해줘야 함. (처음에 1로 해주니 detail페이지에 1로 출력) -->
          </select><br>
          <label for="score">SCORE</label>
          <input type="text" id="score" name="score"><br>
          <label for="poster_url">POSTER_URL</label>
          <input type="text" id="poster_url" name="poster_url"><br>
          <label for="description">DESCRIPTION</label>
          <textarea name="description" id="description"></textarea><br> <!-- textarea로 -->
          <input type="submit" value="Submit"> <!-- type을 submit으로 해주면 알아서 버튼처럼 생김, value는 글씨를 바꿔주는 기능 -->
          <hr>
      </form>
      <a href="{% url 'movies:index' %}">BACK</a> 
  {% endblock content %}
  ```

  - 이 문제에서 어려웠던 점
    * form을 작성하면서 text가 아닌 date, select, textarea 등등 경험
    * create view 함수로 온 후에 1. POST로 받은 값들을 변수에 저장, 2. 인스턴스 생성 후 작성 및 저장 즉, 2단계로 생각하기 
  - 내가 생각하는 이 문제의 포인트 
    * POST한 값을 create로 보내주고 create에서 받아서 저장 후 index창으로 보여주는 것

------

 

## E. edit.html

* 요구 사항: 
  * 영화 수정 페이지

- 결과 : 

  - 문제 접근 방법 및 코드 설명
    * 특정 영화 수정하기 위한 form 작성
    * input 요소에는 기존 데이터 출력
    * Reset 버튼은 사용자의 모든 입력을 초기 값으로 재설정
    * 작성한 정보는 제출(submit) 시 단일 영화 데이터를 수정하는 URL로 요청과 함께 전송
    * detail.html로 이동하는 링크 표시

  ```python
  # movies/urls.py
  from django.urls import path
  from . import views 
  
  app_name = 'movies'
  urlpatterns = [
      path('', views.index, name='index'),
      path('<int:pk>/', views.detail, name='detail'), # 각각의 영화마다 페이지가 필요하므로 뒤에 pk값을 붙임
      path('new/', views.new, name='new'),
      path('create/', views.create, name='create'),
      path('<int:pk>/edit', views.edit, name='edit'),
      path('<int:pk>/update', views.update, name='update'),
      path('<int:pk>/delete', views.delete, name='delete'),
  ]
  
  # movies/views.py
  from django.shortcuts import render, redirect
  from .models import Movie
  
  def index(request):
      movies = Movie.objects.all() # 모든 영화 조회
      context = {
          'movies' : movies
      } # movies/index.html에 {{  }} 쓰이므로 여기서 정의 내려줘야 함.
      return render(request, 'movies/index.html', context)
  
  def detail(request, pk):
      movie = Movie.objects.get(pk=pk) # 특정 pk값이 들어오면 그 pk를 가진 레코드를 movie에 넣기
      context = {
          'movie' : movie
      }
      return render(request, 'movies/detail.html', context)
  
  def new(request):
      return render(request, 'movies/new.html')
  
  def create(request): 
      title = request.POST.get('title') # POST로 받은 정보들을 각각 변수에 저장, 괄호 안의 값은 form 태그 안의 name 값을 적어줘야 함(따옴표 주의)
      audience = request.POST.get('audience')
      release_date = request.POST.get('release_date')
      genre = request.POST.get('genre')
      score = request.POST.get('score')
      poster_url = request.POST.get('poster_url')
      description = request.POST.get('description')
  
      # movie라는 인스턴스 생성하면서 받은 값을 필드에 맞춰 작성 & 저장
      movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
      movie.save()
      return redirect('movies:index') # 저장 끝나면 index창으로 감. redirect 이용
  
  def edit(request, pk): # detail.html에서 EDIT 클릭 시 urls 거쳐 여기로 옴.
      movie = Movie.objects.get(pk=pk) # detail.html에서 가지고 있던 pk가 들어오게 됨. 그 row를 movie에 담아줌
      context = {
          'movie' : movie
      }
      return render(request, 'movies/edit.html', context)
  
  def update(request, pk):
      # 생성 방식 중 1번 방식이랑 비슷
      movie = Movie.objects.get(pk=pk) # edit.html에서 가지고 있던 pk 값으로 row 조회 후 movie에 넣어줌
      # context = {
      #     'movie' : movie
      # }
      # update.html이 따로 없기에 적어줄 필요 없음
  
      # movie. 붙여주기
      movie.title = request.POST.get('title')
      movie.audience = request.POST.get('audience')
      movie.release_date = request.POST.get('release_date')
      movie.genre = request.POST.get('genre')
      movie.score = request.POST.get('score')
      movie.poster_url = request.POST.get('poster_url')
      movie.description = request.POST.get('description')
  
      # movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description) 이러면 새로 생성됨
      movie.save()
      return redirect('movies:detail', movie.pk) # detail은 인자가 하나 더 필요함
  
  def delete(request, pk):
      movie = Movie.objects.get(pk=pk)
      movie.delete()
      return redirect('movies:index')
  ```

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
      <h1 class="fw-bold">EDIT</h1>
      <hr>
      <form action="{% url 'movies:update' movie.pk %}" method="POST"> <!-- new처럼 edit은 정보를 입력받는 곳, create처럼 update가 받은 정보를 수정해주는 곳 -->
          {% csrf_token %}
          <label for="title">TITLE</label>
          <input type="text" id="title" name="title" value="{{movie.title}}"><br> <!-- value를 넣어주면 edit.html 열면 value값으로 채워져 있음. 원래 있었던 값으로 넣어주고자 중괄호 2개 가져옴 -->
          <label for="audience">AUDIENCE</label>
          <input type="text" id="audience" name="audience" value="{{movie.audience}}"><br>
          <label for="release_date">RELEASE_DATE</label>
          <input type="date" id="release_date" name="release_date" value="{{movie.release_date|date:"Y-m-d"}}"><br> <!-- movie.release_date 이거만 넣으면 안 됨 -->
          <label for="genre">GENRE</label>
          <select id="genre" name="genre"> <!-- select 사용 -->
              <option value="코미디">코미디</option>
          </select><br>
          <label for="score">SCORE</label>
          <input type="text" id="score" name="score" value="{{movie.score}}"><br>
          <label for="poster_url">POSTER_URL</label>
          <input type="text" id="poster_url" name="poster_url" value="{{movie.poster_url}}"><br>
          <label for="description">DESCRIPTION</label>
          <textarea name="description" id="description">{{movie.description}}</textarea><br> <!-- textarea는 value를 안에 넣으면 안 되고 밖에 작성해줘야 함 -->
          <input type="reset" value="Reset"> <!-- input type이 reset이면 초기 값으로 재설정해줌 -->
          <input type="submit" value="Submit">
          <hr>
      </form>
      <a href="{% url 'movies:detail' movie.pk %}">BACK</a> 
  {% endblock content %}
  ```

  - 이 문제에서 어려웠던 점
    * form 작성할 때 기존데이터를 남기는 작업 중 date 때문에 애먹었음.
    * reset은 생각보다 간단했으나 잘 몰라서 조금 돌아감
    * edit에서 POST한 값을 update view 함수로 가져왔는데 생성 2번째 방식과 비슷하게 하려니 진짜로 하나가 더 만들어지는 로직을 짜버림. 생성 1번째 방식을 생각해서 다시 짜봄(1. 기존 pk로 get하여 수정할 movie row를 받고 2. movie.필드 로 접근하여 수정 후 3. 저장)
  - 내가 생각하는 이 문제의 포인트 
    * new-create와 같이 2개의 view함수가 필요하다는 점!

------



# 후기

- 어렵다기 보다는 너무나도 새로워서.. 그래도 하다보니 생각하게 되고 생각하게 되니 이해가 되고.. 오늘 안에 완료해서 다행! 
- 주말에도 한 번 더 만들어보자! 익숙하게!