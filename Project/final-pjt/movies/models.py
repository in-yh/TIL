from django.db import models
from django.conf import settings


class Genre(models.Model):
    genre_num = models.IntegerField()
    name = models.CharField(max_length=100)


class Movie(models.Model):
    movie_num = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.DateTimeField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_avg = models.FloatField()
    overview = models.TextField(blank=True)
    poster_path = models.TextField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
    click_count = models.IntegerField(null=True)
    click_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="click_movies")
    
    
class Detail(models.Model):    
    movie_num = models.IntegerField()
    backdrop_path = models.TextField(blank=True, null=True)
    production_countries = models.CharField(max_length=100)