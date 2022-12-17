from django.urls import path

from .views import (
    UserAPIView, UserDetailAPIView,

    DocumentAPIView, DocumentDetailAPIView,

    CatalogAPIView, CatalogDetailAPIView
)

urlpatterns = [
    ###  User Api
    path('user/', UserAPIView.as_view(), name='user_api'),
    path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail_api'),


    ### Document Api
    path('documents/', DocumentAPIView.as_view(), name='document_api'),
    path('documents/<int:pk>/', DocumentDetailAPIView.as_view(), name='document_detail_api'),


    ### Catalog Api
    path('catalog/', CatalogAPIView.as_view(), name='catalog_api'),
    path('catalog/<int:pk>/', CatalogDetailAPIView.as_view(), name='catalog_detail_api'),

]

