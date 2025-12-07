from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('achievements/', views.achievements, name='achievements'),
    path('profile/', views.profile, name='profile'),
]