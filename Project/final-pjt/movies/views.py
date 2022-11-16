from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
from .models import Genre

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
    context = {
        'results': results,
    }
    return render(request, 'movies/category_genre.html', context)