from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/genre/', views.category_genre, name='category_genre'),
    path('category/genre/<str:genre_name>/', views.category_genre_detail, name='category_genre_detail'),
    path('movie/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
]