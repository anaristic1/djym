from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Exercise, ExerciseType
from .forms import ExeForm


def home(request):
    print(request.user)
    return render(request, 'gym/home.html')


@login_required
def login_user(request):
    pass


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


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


def view_exercise(request, exercise_pk):
    exercise = get_object_or_404(Exercise, pk=exercise_pk)

    if request.method == 'GET':
        form = ExeForm(instance=exercise)
        return render(request, 'gym/exercise.html', {'exercise': exercise, 'form': form})
    else:
        try:
            form = ExeForm(request.POST, instance=exercise)
            form.save()
            return redirect('all_exercises')
        except ValueError as e:
            return render(request, 'gym/exercise.html', {'exercise': exercise, 'form': form, 'error': e})


def delete_exercise(request, exercise_pk):
    exercise = get_object_or_404(Exercise, pk=exercise_pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('all_exercises')
