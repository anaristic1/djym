from django.db import models
from django.contrib.auth.models import User


class ExerciseType(models.Model):
    type = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.type


class Exercise(models.Model):
    name = models.CharField(max_length=80)
    type = models.ForeignKey(ExerciseType, on_delete=models.PROTECT)
    video = models.URLField(blank=True)

    def __str__(self):
        return self.name


class ExerciseInfo(models.Model):
    exercise = models.OneToOneField(
        Exercise,
        on_delete=models.PROTECT,
    )
    num_of_sets = models.IntegerField(default=1)
    reps = models.CharField(max_length=20)
    equipment = models.CharField(max_length=40, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.exercise} {self.num_of_sets} sets {self.reps} reps'


class Workout(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True, blank=True)
    exercises = models.ManyToManyField(ExerciseInfo)
