from django.contrib import admin
from .models import ExerciseType, Exercise, ExerciseInfo, Workout

admin.site.register(Exercise)
admin.site.register(ExerciseType)
admin.site.register(ExerciseInfo)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    exclude = ('date_updated',)
