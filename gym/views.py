from django.shortcuts import render, get_object_or_404
from .models import Exercise, ExerciseType


def home(request):
    return render(request, 'gym/home.html')


def all_exercises(request, workout_type=''):
    message = ''
    exercise_type = ExerciseType.objects.all()
    if workout_type:
        exercises = Exercise.objects.filter(type=ExerciseType.objects.get(type=workout_type))
        if not exercises:
            message = f'There are no exercises with type {workout_type}'
    else:
        exercises = Exercise.objects.all()

    return render(request, 'gym/exercises.html', {'exercises': exercises, 'e_type': exercise_type, 'message': message })
