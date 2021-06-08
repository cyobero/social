from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.user_register, name='user_register'),
    path('profile/<username>', views.user_profile, name='user_profile'),
    path('profile/update/<pk>',
         login_required(views.ProfileUpdateView.as_view()), name='update_profile'),
    path('', views.dashboard, name='dashboard'),
]
