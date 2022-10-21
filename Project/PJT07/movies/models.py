from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    # movies = models.ManyToManyField(Movie, related_name='actors') # 이러면 Movie 모델 먼저 써줘야해


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies') # movies_movie_actors 테이블 생김 


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

# migrate 이후 
# python manage.py loaddata movies/actors.json movies/movies.json movies/reviews.json