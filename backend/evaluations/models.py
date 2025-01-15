from django.db import models
import uuid
from django.utils import timezone



class Player(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    team = models.CharField(max_length=100, null=True, blank=True)
    points_per_game = models.FloatField(default=0.0)
    rebounds_per_game = models.FloatField(default=0.0)
    assists_per_game = models.FloatField(default=0.0)
    steals_per_game = models.FloatField(default=0.0)
    blocks_per_game = models.FloatField(default=0.0)
    turnovers_per_game = models.FloatField(default=0.0)
    field_goals_made = models.FloatField(default=0.0)
    field_goals_att = models.FloatField(default=0.0)
    three_points_made = models.FloatField(default=0.0)
    three_points_att = models.FloatField(default=0.0)
    free_throws_made = models.FloatField(default=0.0)
    free_throws_att = models.FloatField(default=0.0)
    efficiency = models.FloatField(default=0.0)
    headshot = models.ImageField(upload_to='player_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    defensive_score = models.IntegerField()
    passing_score = models.IntegerField()
    scoring_score = models.IntegerField()
    iq_score = models.IntegerField()
    final_grade = models.CharField(max_length=2)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created
    updated_at = models.DateTimeField(auto_now=True)      # Automatically updated on save


class Weight(models.Model):
    category = models.CharField(max_length=50)
    value = models.FloatField()  # Weight percentage


