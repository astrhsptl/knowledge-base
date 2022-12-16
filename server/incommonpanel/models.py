from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Catalog(models.Model):
    title = models.CharField(max_length=20,)

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogs'
        #ordering = []

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse_lazy('catalog_detail', kwargs={'pk' : self.pk})

class Document(models.Model):
    title = models.CharField(max_length=30,)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    private_access = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    catalog = models.ForeignKey(Catalog, default=None, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('document_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        #ordering = []