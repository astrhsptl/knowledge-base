from django.urls import path

from .views import (
    # Preview/admin update system
    ModeratorUserDetailView, ModeratorUserUpdateView,

    DocumentCreationsView, CatalogCreationalView,

    user_register,
    )

urlpatterns = [
    path('user/<int:pk>/', ModeratorUserDetailView.as_view(), name='moder_user_detail'),
    path('user/<int:pk>/update/', ModeratorUserUpdateView.as_view(), name='moder_user_update'),

    path('document/creational/', DocumentCreationsView.as_view(), name='moder_document_creational'),
    path('catalog/creational/', CatalogCreationalView.as_view(), name='moder_document_creational'),

    path('register/', user_register, name='register'),
]