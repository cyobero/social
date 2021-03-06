from django.urls import path

from . import views

urlpatterns = [
    path('requests/', views.friend_requests, name='friend_requests'),
    path('requests/accept/', views.friend_accept, name='friend_accept'),
    path('requests/reject/', views.friend_reject, name='friend_reject'),
]
