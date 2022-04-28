from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=222)
    active=models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class StreamPlatform(models.Model):
    name=models.CharField(max_length=22)
    about=models.CharField(max_length=222)
    website=models.URLField(max_length=222)

    def __str__(self) -> str:
        return self.name

class WatchList(models.Model):
    title=models.CharField(max_length=222)
    storyline=models.CharField(max_length=222)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
        
