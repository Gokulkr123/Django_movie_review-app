from .models import Movie
from django import forms

class MovieForm(forms.ModelForm):
    class Meta:
        model= Movie
        fields = ['movie_name', 'movie_poster', 'release_date', 'rating', 'review']