from django.db import models
from django.forms import CharField

# Create your models here.
class Genre(models.Model):
    genre = CharField


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    vote_average = models.FloatField()
    poster_path = models.CharField(max_length=100)
    popularity = models.FloatField()
    release_date=models.DateField()
    genres = models.ManyToManyField(Genre)