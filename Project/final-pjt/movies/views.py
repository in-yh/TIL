from django.shortcuts import render
from django.db.models import Count
from .models import Genre, Movie
import json, random

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