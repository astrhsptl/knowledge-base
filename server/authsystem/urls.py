from django.urls import path

from .views import (
    # Authentications system
    user_login,  user_logout,

    # User Account system    
    UserDetailView, UserUpdateView,
    )

urlpatterns = [
    #       User Account
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('user/update/', UserUpdateView.as_view(), name='user_update'),

    #       Authenticate system
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]