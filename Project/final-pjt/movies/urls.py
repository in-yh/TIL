from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/genre/', views.category_genre, name='category_genre'),
]