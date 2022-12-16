from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from .models import (
    Catalog, Document
)


###     Homepage
class HomePageListView(ListView):
    model = Catalog
    template_name = 'incommon_templates/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['user'] = self.request.user
        return context


###     Catalog 
class CatalogsListView(ListView):
    model = Catalog
    template_name = 'incommon_templates/catalog/catalog_list.html'
    context_object_name = 'catalogs'

class CatalogDetailView(DetailView):
    model = Catalog
    template_name = 'incommon_templates/catalog/catalog_detail.html'
    context_object_name = 'catalog'

class CatalogUpdateView(UpdateView):
    model = Catalog
    fields = ['title']
    context_object_name = 'catalog'
    template_name = 'incommon_templates/catalog/catalog_update.html'
    

###         Document
class DocumentsListView(ListView):
    model = Document
    template_name = 'incommon_templates/document/documents_list.html'
    context_object_name = 'documents'

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'incommon_templates/document/document_detail.html'
    context_object_name = 'document'

class DocumentUpdateView(UpdateView):
    model = Document
    fields = ['title', 'file', 'private_access', 'catalog']
    context_object_name = 'catalog'
    template_name = 'incommon_templates/document/document_update.html'
    
