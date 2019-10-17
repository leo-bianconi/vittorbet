from django.shortcuts import render
from django.http import HttpResponse
from .models import Match
import datetime
from django.utils import timezone
import pytz

# Create your views here.

def homepage_view(request):
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min, tzinfo=pytz.UTC)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max, tzinfo=pytz.UTC)
    match_list = Match.objects.all().filter(date__range=(today_min, today_max))
    return render(request, 'matches/index.html', {'match_list': match_list})
