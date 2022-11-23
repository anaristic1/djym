from django.db import models


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
