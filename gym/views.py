from django.shortcuts import render
from .models import Exercise


def home(request):
    return render(request, 'gym/home.html')


def all_exercises(request):
    exercises = Exercise.objects.all()
    return render(request, 'gym/exercises.html', {'exercises': exercises})
