from django.contrib import admin
from django.urls import path, include
from . import views

appname = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('change-pass/', views.change_pass_view, name='change-pass'),
    path('logout/', views.logout_view, name='logout'),
]
