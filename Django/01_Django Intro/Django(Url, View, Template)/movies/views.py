from django.shortcuts import render

def home(request):
    movie = ['topgun', 'spiderman']

    context = {
        'movie' : movie,
    }
    return render(request, 'movies/home.html', context)
