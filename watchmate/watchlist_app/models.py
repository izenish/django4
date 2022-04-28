
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
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
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")

    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title 

class Review(models.Model):
    rating=models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=222,null=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name="review")
    active=models.BooleanField(default=True)


    def __str__(self) -> str:
        # return str(self.rating) + " " +self.watchlist.title
        return f'{str(self.rating)} ⭐️ {self.watchlist.title} '
