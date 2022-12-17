from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
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
class CatalogsListView(ListView, LoginRequiredMixin):
    model = Catalog
    template_name = 'incommon_templates/catalog/catalog_list.html'
    context_object_name = 'catalogs'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.private_access:
            return queryset
        else:
            queryset = self.model.objects.raw("""
            SELECT cat.*, doc.* FROM incommonpanel_catalog AS cat 
            JOIN incommonpanel_document AS doc 
            ON doc.private_access == 0 AND doc.catalog_id == cat.id;
            """)
        return queryset

class CatalogDetailView(DetailView, LoginRequiredMixin):
    model = Catalog
    template_name = 'incommon_templates/catalog/catalog_detail.html'
    context_object_name = 'catalog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.private_access:
            context['documents'] = Document.objects.filter(
                catalog=context['catalog'], )
        else:
            context['documents'] = Document.objects.filter(
                catalog=context['catalog'], 
                private_access=False,)

        return context


class CatalogUpdateView(UpdateView, LoginRequiredMixin):
    model = Catalog
    fields = ['title']
    context_object_name = 'catalog'
    template_name = 'incommon_templates/catalog/catalog_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        print(context['user'].is_staff)
        return context
    

###         Document
class DocumentsListView(ListView, LoginRequiredMixin):
    model = Document
    template_name = 'incommon_templates/document/documents_list.html'
    context_object_name = 'documents'

    def get_queryset(self):
        if self.request.user.private_access:
            return super().get_queryset()
        else:
            return self.model.objects.filter(private_access=False) 

class DocumentDetailView(DetailView, LoginRequiredMixin):
    model = Document
    template_name = 'incommon_templates/document/document_detail.html'
    context_object_name = 'document'

class DocumentUpdateView(UpdateView, LoginRequiredMixin):
    model = Document
    fields = ['title', 'file', 'private_access', 'catalog']
    context_object_name = 'catalog'
    template_name = 'incommon_templates/document/document_update.html'
    
