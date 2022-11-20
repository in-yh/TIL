from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/genre/', views.category_genre, name='category_genre'),
    path('category/genre/<str:genre_name>/', views.category_genre_detail, name='category_genre_detail'),
    path('movie/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('category/era/', views.category_era, name='category_era'),
    path('category/era/<str:era>/', views.category_era_detail, name='category_era_detail'),
    path('category/country/', views.category_country, name='category_country'),
    path('category/country/<str:country>/', views.category_country_detail, name='category_country_detail'),
    path('movie/<int:movie_pk>/click/', views.movie_click, name='movie_click'),
    path('movie/recommend/', views.movie_recommend, name='movie_recommend'),
]