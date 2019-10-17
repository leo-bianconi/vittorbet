from django.contrib import admin
from .models import Match, Player, Team, Tournament

admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Tournament)
