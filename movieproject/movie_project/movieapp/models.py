from django.db import models

# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=100)
    language=models.TextField()
    genre=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    desc=models.TextField()
    cast1=models.CharField(max_length=150)
    cast2=models.CharField(max_length=150)
