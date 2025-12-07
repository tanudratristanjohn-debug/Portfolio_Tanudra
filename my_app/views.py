from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def achievements(request):
    return render(request, 'achievements.html')

def profile(request):
    return render(request, 'profile.html')