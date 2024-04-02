from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=500)
    movie_poster = models.URLField(max_length=200, null=True, blank=True)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0), MaxValueValidator(10)])
    review = models.TextField()
