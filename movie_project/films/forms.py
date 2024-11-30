from .models import Films
from django.forms import ModelForm


class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'description', 'review']

