from django.forms import ModelForm
from .models import Exercise


class ExeForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'type', 'video']