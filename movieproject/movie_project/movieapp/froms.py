from django import forms
from.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','language','genre','year','img','desc','cast1','cast2']