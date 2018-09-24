from django.db import models


class Game(models.Model):
    player = models.CharField(max_length=100, default='Unknown')
    date = models.DateField(auto_now_add=True)
    time = models.IntegerField(default=0)
    guesses = models.IntegerField(default=0)

    def __str__(self):
        return self.player


class MemoCard(models.Model):
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=300)
    theme = models.CharField(max_length=100)


class Deck(models.Model):
    theme = models.CharField(max_length=100)
    cards = models.ManyToManyField(MemoCard)
    size = models.IntegerField(default=0)

    def __str__(self):
        return self.theme


