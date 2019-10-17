from django.db import models
from datetime import datetime

GAMES = [
    ('CS:GO', 'Counter-Strike: Global Offensive'),
]

class Match(models.Model):
    team1 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='team2')
    score1 = models.PositiveIntegerField(default=0)
    score2 = models.PositiveIntegerField(default=0)
    game = models.CharField(max_length=100, choices=GAMES)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    tournament = models.ForeignKey('Tournament', on_delete=models.CASCADE) #aggiungere default
    stream = models.URLField(max_length=300)

    def __str__(self):
        return f"{self.date} - {self.team1} vs. {self.team2}"

    def get_hour(self):
        return self.date.strftime("%H:%M")

    def get_score(self):
        return f"{self.score1} - {self.score2}"     #da sistemare


class Team(models.Model):
    name = models.CharField(max_length=100)
    date_founded = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=100)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True) #null per resettare lo status di un player quando esce dal team

    def __str__(self):
        return self.nickname


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name
