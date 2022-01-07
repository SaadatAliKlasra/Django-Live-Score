from django.db import models

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="away_team"
    )
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="local_team"
    )
    home_goals = models.PositiveSmallIntegerField(default=0)
    away_goals = models.PositiveSmallIntegerField(default=0)
    game_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
