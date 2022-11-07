import random
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_safe
from .models import Movie


@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    # movie = get_object_or_404(Movie.objects.prefetch_related('genres'), pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    movies = Movie.objects.all()
    recommended_movies = random.sample(list(movies), 10)  # 랜덤 영화 10개 추천
    context = {
        'recommended_movies': recommended_movies,
    }
    return render(request, 'movies/recommended.html', context)