from django.db import models
import uuid
from django.utils import timezone



class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=50, null=True, blank=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)

    # Performance Statistics
    points_per_game = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rebounds_per_game = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    assists_per_game = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    steals_per_game = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    blocks_per_game = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    turnovers_per_game = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Efficiency
    field_goal_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    three_point_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    free_throw_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    efficiency_rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Advanced Stats
    true_shooting_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    usage_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

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


