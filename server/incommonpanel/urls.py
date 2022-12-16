from django.urls import path

from .views import (
    HomePageListView,

    ###  Catalogs
    CatalogsListView, CatalogDetailView, CatalogUpdateView,

    ###  Documents
    DocumentsListView, DocumentDetailView, DocumentUpdateView,
)

urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),

    ###    Catalogs urls
    path('catalogs/', CatalogsListView.as_view(), name='catalog_list'),
    path('catalogs/<int:pk>/', CatalogDetailView.as_view(), name='catalog_detail'),
    path('catalogs/<int:pk>/update/', CatalogUpdateView.as_view(), name='catalog_update'),

    ###    Documents urls
    path('documents/', DocumentsListView.as_view(), name='document_list'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
    path('documents/<int:pk>/update/', DocumentUpdateView.as_view(), name='document_update'),]