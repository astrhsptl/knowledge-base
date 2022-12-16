from django.urls import path

from .views import (
    # Preview/admin update system
    ModeratorUserDetailView, ModeratorUserUpdateView,
    user_register,
    )

urlpatterns = [
    path('<int:pk>/', ModeratorUserDetailView.as_view(), name='moder_user_detail'),
    path('<int:pk>/update/', ModeratorUserUpdateView.as_view(), name='moder_user_update'),

    path('register/', user_register, name='register'),
]