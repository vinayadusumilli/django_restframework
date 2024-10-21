from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=150)
    url = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=100)
    storyline = models.CharField(max_length=250)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="platform")
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    review = models.CharField(max_length=200)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='watchlist')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.rating) + ' | ' + self.watchlist.title
