from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    height = models.CharField(max_length=10)
    image = models.ImageField(upload_to='player_images/', null=True, blank=True)

class Evaluation(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    defensive_score = models.IntegerField()
    passing_score = models.IntegerField()
    scoring_score = models.IntegerField()
    iq_score = models.IntegerField()
    final_grade = models.CharField(max_length=2)

class Weight(models.Model):
    category = models.CharField(max_length=50)
    value = models.FloatField()  # Weight percentage

