from django.forms import ModelForm

from .models import Catalog

class CatalogForm(ModelForm):
    class Meta:
        model = Catalog
        fields = ['title',]