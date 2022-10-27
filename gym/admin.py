from django.contrib import admin
from .models import ExerciseType, Exercise


admin.site.register(Exercise)
admin.site.register(ExerciseType)
