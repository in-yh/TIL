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
    movie = Movie.objects.get(pk=pk) # 그 행 가져온 다음
    movie.delete() # 삭제
    return redirect('movies:index')