import os
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView

from .models import (
    Catalog, Document
)
from server.settings import MEDIA_ROOT
from buisneslogic.preprocess_files import docx2html, preprocess_excel_table


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
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagination_range'] = list(context['page_obj'].paginator.page_range)
        return context

    def get_queryset(self):
        if self.request.user.private_access:
            return super().get_queryset()
        else:
            return self.model.objects.filter(private_access=False) 

class DocumentUpdateView(UpdateView, LoginRequiredMixin):
    model = Document
    fields = ['title', 'file', 'private_access', 'catalog']
    context_object_name = 'catalog'
    template_name = 'incommon_templates/document/document_update.html'
    
class DocumentDetailView(DetailView, LoginRequiredMixin):
    model = Document
    template_name = 'incommon_templates/document/document_detail.html'
    context_object_name = 'document'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        file_path = os.path.join('/media', str(context['document'].file))
        file_expansion = str(context['document'].file).split('/')[-1].split('.')[-1]
        
        # print(file_path, file_expansion, sep='\n')
        
        context['image_expantions'] = ['png', 'jpeg', 'jpg', ]
        context['presentation_expantions'] = ['pptx', 'ppt', ]
        context['text_expantions'] = ['docx', 'doc', 'text', ]
        context['table_expantions'] = ['xlsx', 'csv', 'xls', ]
        context['file_expansion'] = file_expansion
        context['file_path'] = str(file_path)

        if context['file_expansion'] in context['text_expantions']:
            try:
                context['docx_text'] = docx2html(os.path.join(MEDIA_ROOT, str(context['document'].file)))
            except:
                context['docx_text'] = 'что-то пошло не так'
        elif context['file_expansion'] in context['table_expantions']:
            try:
                excel_data, worksheet = preprocess_excel_table(os.path.join(MEDIA_ROOT, str(context['document'].file)))
                context['excel_data'] = excel_data
                context['worksheet'] = worksheet
            except:
                context['docx_text'] = 'что-то пошло не так'

        # print(context)
        
        return context