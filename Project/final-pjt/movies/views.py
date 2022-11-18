from django.shortcuts import render
from django.db.models import Count
from .models import Genre, Movie
import json, random, datetime
from django.db.models.functions import TruncYear

# @require_safe
def index(request): 
    return render(request, 'movies/index.html') 


def category_genre(request):
    # 장르별 영화 개수 조회
    movies_counts = Genre.objects.annotate(Count("movies"))
    # print(movies_counts[4].movies__count)
    # print(movies_counts[4].pk)
    # movies_counts : <QuerySet [<Genre: Genre object (12)>, <Genre: Genre object (14)>, <Genre: Genre object (16)>, ...

    results = []
    for q in movies_counts:
        specific_genre = Genre.objects.get(pk=q.pk)
        results.append(
            {
                'x': specific_genre.name, 
                'value': q.movies__count
            }
        )
    j_results = json.dumps(results) # json으로 담기
    context = {
        'j_results': j_results,
    }
    return render(request, 'movies/category_genre.html', context)
    

def category_genre_detail(request, genre_name):
    genre = Genre.objects.get(name=genre_name)
    movies = genre.movies.all()
    random_movies = random.choices(movies, k=40)

    movies_dict = []
    for movie in random_movies:
        movies_dict.append(
            {
                'x': movie.title, 
                'y': movie.pk, # 영화 디테일 페이지로 들어가기 위해 필요
                'value' : movie.vote_avg
            }
        )
    j_results = json.dumps(movies_dict)
    context = {
        'j_results': j_results,
    }
    return render(request, 'movies/category_genre_detail.html', context)


def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    movie_information = [
        {'x': movie.title, 'y': movie.poster_path, 'value' : 100},
        {'x': movie.vote_avg, 'y': movie.poster_path, 'value' : 100},
        {'x': movie.popularity, 'y': movie.poster_path, 'value' : 100},
        {'x': str(movie.released_date)[0:10], 'y': movie.poster_path, 'value' : 100},
        # {'x': str(movie.overview), 'value' : 100},
    ]
    j_results = json.dumps(movie_information)
    context = {
        'j_results': j_results,
    }
    return render(request, 'movies/movie_detail.html', context)


def category_era(request):
    # 시대별 영화개수 구하기

    # 먼저, 년도별 영화개수 구하기
    # Trunc는 중요한 구성 요소까지 날짜를 자른다는 의미 / TruncYear은 년도까지만 자른다. 즉, released_date가 2022-11-18이면 TruncYear('released_date')는 2022-01-01이 된다. 
    years_countmovies = Movie.objects.annotate(year=TruncYear('released_date')).values('year').annotate(Count('movie_num'))
    
    # 시대별로 묶어주기
    era_1930, era_1940, era_1950, era_1960, era_1970, era_1980, era_1990, era_2000, era_2010, era_2020 = [0]*10
    for year_countmovies in years_countmovies:
        # print(str(year_countmovies['year'].date())[0:4], year_countmovies['movie_num__count'])
        if str(year_countmovies['year'].date())[0:3] == '193':
            era_1930 += year_countmovies['movie_num__count']
        elif str(year_countmovies['year'].date())[0:3] == '194':
            era_1940 += year_countmovies['movie_num__count']
        elif str(year_countmovies['year'].date())[0:3] == '195':
            era_1950 += year_countmovies['movie_num__count']
        elif str(year_countmovies['year'].date())[0:3] == '196':
            era_1960 += year_countmovies['movie_num__count']
        elif str(year_countmovies['year'].date())[0:3] == '197':
            era_1970 += year_countmovies['movie_num__count']
        elif str(year_countmovies['year'].date())[0:3] == '198':
            era_1980 += year_countmovies['movie_num__count']
        elif str(year_countmovies['year'].date())[0:3] == '199':
            era_1990 += year_countmovies['movie_num__count']
        elif str(year_countmovies['year'].date())[0:3] == '200':
            era_2000 += year_countmovies['movie_num__count']
        elif str(year_countmovies['year'].date())[0:3] == '201':
            era_2010 += year_countmovies['movie_num__count']
        elif str(year_countmovies['year'].date())[0:3] == '202':
            era_2020 += year_countmovies['movie_num__count']

    era_information = [
        {'x': '1930s', 'value' : era_1930},
        {'x': '1940s', 'value' : era_1940},
        {'x': '1950s', 'value' : era_1950},
        {'x': '1960s', 'value' : era_1960},
        {'x': '1970s', 'value' : era_1970},
        {'x': '1980s', 'value' : era_1980},
        {'x': '1990s', 'value' : era_1990},
        {'x': '2000s', 'value' : era_2000},
        {'x': '2010s', 'value' : era_2010},
        {'x': '2020s', 'value' : era_2020},
    ]

    j_results = json.dumps(era_information)
    context = {
        'j_results': j_results,
    }
    return render(request, 'movies/category_era.html', context)


def category_era_detail(request, era):
    # 시대별 영화 제목 랜덤으로 뽑기
    era_number = int(era[0:4])
    startdate = datetime.date(era_number, 1, 1)
    enddate = datetime.date(era_number+10, 1, 1)

    era_movies = Movie.objects.filter(released_date__range=[startdate, enddate])
    random_movies = random.choices(era_movies, k=40)

    movies_dict = []
    for movie in random_movies:
        movies_dict.append(
            {
                'x': movie.title, 
                'y': movie.pk, # 영화 디테일 페이지로 들어가기 위해 필요
                'value' : movie.vote_avg
            }
        )
    j_results = json.dumps(movies_dict)
    context = {
        'j_results': j_results,
    }
    return render(request, 'movies/category_era_detail.html', context)