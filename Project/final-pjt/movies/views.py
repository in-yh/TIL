from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Genre, Movie, Detail
import json, random, datetime
from django.db.models.functions import TruncYear


# @require_safe
def index(request): 
    return render(request, 'movies/index.html') 


def category_genre(request):
    if request.user.is_authenticated: 
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
    return redirect('accounts:login')
    

def category_genre_detail(request, genre_name):
    if request.user.is_authenticated:
        genre = Genre.objects.get(name=genre_name)
        movies = genre.movies.all()
        random_movies = random.choices(movies, k=20)

        movies_dict = []
        for movie in random_movies:
            movies_dict.append(
                {
                    'x': movie.title, 
                    'y': movie.pk, # 영화 디테일 페이지로 들어가기 위해 필요
                    'value' : movie.vote_avg*30
                }
            )
        j_results = json.dumps(movies_dict)
        context = {
            'genre': genre,
            'j_results': j_results,
        }
        return render(request, 'movies/category_genre_detail.html', context)
    return redirect('accounts:login')


def movie_detail(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        detail = Detail.objects.get(pk=movie_pk)

        # 유저가 무비 클릭하면 유저id-무비id 저장  
        request.user.click_movies.add(movie_pk)
        
        genre_list = ''
        genres = movie.genres.all()
        for genre in genres:
            genre_list = genre_list + ' ' + genre.name

        movie_information = [
            {'x': f'title : {movie.title}', 'y': movie.poster_path, 'value' : 100},
            {'x': f'vote average : {movie.vote_avg}', 'y': movie.poster_path, 'value' : 100},
            {'x': f'popularity : {movie.popularity}', 'y': movie.poster_path, 'value' : 100},
            {'x': f'released date : {str(movie.released_date)[0:10]}', 'y': movie.poster_path, 'value' : 100},
            {'x': f'overview : {movie.overview}', 'y': movie.poster_path, 'value' : 50},
            {'x': f'genre : {genre_list}', 'y': movie.poster_path, 'value' : 100},
            {'x': f'country : {detail.production_countries}', 'y': movie.poster_path, 'value' : 100},

        ]
        j_results = json.dumps(movie_information)
        context = {
            'j_results': j_results,
            'detail' : detail,
        }
        return render(request, 'movies/movie_detail.html', context)
    return redirect('accounts:login')


def category_era(request):
    if request.user.is_authenticated: 
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
    return redirect('accounts:login')


def category_era_detail(request, era):
    if request.user.is_authenticated:
        # 시대별 영화 제목 랜덤으로 뽑기
        era_number = int(era[0:4])
        startdate = datetime.date(era_number, 1, 1)
        enddate = datetime.date(era_number+10, 1, 1)

        era_movies = Movie.objects.filter(released_date__range=[startdate, enddate])
        if era_movies.count() < 20:
            random_movies = random.choices(era_movies, k=era_movies.count())
        else:
            random_movies = random.choices(era_movies, k=20)

        movies_dict = []
        for movie in random_movies:
            movies_dict.append(
                {
                    'x': movie.title, 
                    'y': movie.pk, # 영화 디테일 페이지로 들어가기 위해 필요
                    'value' : movie.vote_avg*30
                }
            )
        j_results = json.dumps(movies_dict)
        context = {
            'j_results': j_results,
            'era_number': era_number,
        }
        return render(request, 'movies/category_era_detail.html', context)
    return redirect('accounts:login')


def category_country(request):
    if request.user.is_authenticated: 
        country_countmovies = Detail.objects.values('production_countries').annotate(Count('pk'))
        # <QuerySet [{'production_countries': 'Argentina', 'pk__count': 26}, {'production_countries': 'Australia', 'pk__count': 57}, ...
        results = []
        for country_countmovie in country_countmovies:
            results.append(
                {
                    'x': country_countmovie['production_countries'], 
                    # 'y':
                    'value': country_countmovie['pk__count'],
                }
            )
        j_results = json.dumps(results) # json으로 담기
        context = {
            'j_results': j_results,
        }
        return render(request, 'movies/category_country.html', context)
    return redirect('accounts:login')


def category_country_detail(request, country): # 맨 처음 영문 대문자로 받아야 함
    if request.user.is_authenticated: 
        country_movies = Detail.objects.filter(production_countries=country)

        if country_movies.count() < 20:
            random_details = random.choices(country_movies, k=country_movies.count())
        else:
            random_details = random.choices(country_movies, k=20)

        movies_dict = []
        for detail in random_details:
            movie = Movie.objects.get(pk=detail.pk)
            movies_dict.append(
                {
                    'x': movie.title, 
                    'y': movie.pk, # 영화 디테일 페이지로 들어가기 위해 필요
                    'value' : movie.vote_avg*30
                }
            )
        j_results = json.dumps(movies_dict)
        context = {
            'j_results': j_results,
            'country': country,
        }
        return render(request, 'movies/category_country_detail.html', context)
    return redirect('accounts:login')


def movie_click(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        movie.click_count += 1
        movie.save() # 저장 반드시 하기
        return redirect('movies:movie_detail', movie_pk)
    return redirect('accounts:login')


def movie_recommend(request):
    if request.user.is_authenticated: 
        movies_click10 = Movie.objects.order_by('-click_count')[:10]

        movies_dict = []
        for movie in movies_click10:
            movies_dict.append(
                {
                    'x': movie.title, 
                    'y': movie.pk, # 영화 디테일 페이지로 들어가기 위해 필요
                    'value' : movie.click_count
                }
            )
        j_results = json.dumps(movies_dict)
        context = {
            'j_results': j_results,
        }
        return render(request, 'movies/recommend.html', context)
    return redirect('accounts:login')

