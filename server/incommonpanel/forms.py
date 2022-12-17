from django import forms
from django.forms import ModelForm

from .models import Catalog

class CatalogForm(ModelForm):
    title = forms.CharField(required=True, min_length=5, max_length=20, )# widget=forms.TextInput(attrs={'class': 'inp'}))
    class Meta:
        model = Catalog
        fields = ('title',)