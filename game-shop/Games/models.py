from django.db import models
from django.urls import reverse
from Account.models import Account
from django.utils import timezone


class Game(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    release_date = models.DateField(default=timezone.now())
    age = models.DecimalField()
    draft = models.BooleanField(default=True) 

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("game_detail", kwargs={"slug": self.slug})
    

class Review(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now())
    recommend = models.BooleanField(default=True)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.game.title + '|' + self.user.email


class ReviewAnswer(models.Model):

    review = models.ForeignKey(Account, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateField(default=timezone.now())

    def __str__(self):
        return 'answer' + '|' + self.user.email


