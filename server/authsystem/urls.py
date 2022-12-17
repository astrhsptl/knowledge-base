from django.urls import path

from .views import (
    # Authentications system
    user_login,  user_logout,

    # User Account system    
    UserDetailView, UserUpdateView, PasswordResetByUser,
    )

urlpatterns = [
    #       User Account
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('user/update/', UserUpdateView.as_view(), name='user_update'),
    path('user/password/reset', PasswordResetByUser.as_view(), name='change_password'),

    #       Authenticate system
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]