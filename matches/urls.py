from django.urls import path
from . import views

app_name = 'matches'

urlpatterns = [
    path('', views.homepage_view, name='index',)
]
