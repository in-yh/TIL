from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
import json, random


def login(request): 
    if request.user.is_authenticated: 
        return redirect('movies:index')

    if request.method == "POST": 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index') 
    else:
        form = AuthenticationForm() 
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('movies:index')


def signup(request): 
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save() 
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request): 
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('movies:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    if request.user.is_authenticated: 
        User = get_user_model()
        person = User.objects.get(username=username)

        movies_dict = []
        like_genres = [
            {'x':'Adventure', 'value':0},
            {'x':'Fantasy', 'value':0},
            {'x':'Animation', 'value':0},
            {'x':'Drama', 'value':0},
            {'x':'Horror', 'value':0},
            {'x':'Action', 'value':0},
            {'x':'Comedy', 'value':0},
            {'x':'History', 'value':0},
            {'x':'Western', 'value':0},
            {'x':'Thriller', 'value':0},
            {'x':'Crime', 'value':0},
            {'x':'Documentary', 'value':0},
            {'x':'Science Fiction', 'value':0},
            {'x':'Mystery', 'value':0},
            {'x':'Music', 'value':0},
            {'x':'Romance', 'value':0},
            {'x':'Family', 'value':0},
            {'x':'War', 'value':0},
            {'x':'TV Movie', 'value':0},
        ]
        for movie in person.click_movies.all():
            movies_dict.append(
                {
                    'x': movie.title, 
                    'y': movie.pk, # 영화 디테일 페이지로 들어가기 위해 필요
                    'value' : movie.vote_avg*30
                }
            )
            for genre in movie.genres.all():
                for like_genre in like_genres:
                    if genre.name == like_genre['x']:
                        like_genre['value'] += 1
        
        like_genres = sorted(like_genres , key= lambda x: x['value'], reverse=True)
        like_genres = like_genres[:5]

        random_movies = random.choices(movies_dict, k=20)

        j_results1 = json.dumps(random_movies)
        j_results2 = json.dumps(like_genres)

        context = {
            'person': person,
            'j_results1': j_results1,
            'j_results2': j_results2,
        }
        return render(request, 'accounts/profile.html', context)
    return redirect('accounts:login')