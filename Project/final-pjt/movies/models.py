from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)
    genre_num = models.IntegerField()

class Movie(models.Model):
    movie_num = models.IntegerField()
    title = models.CharField(max_length=100)
    released_date = models.DateTimeField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies', blank=True)
