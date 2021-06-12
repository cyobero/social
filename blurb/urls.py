from django.urls import path

from . import views

urlpatterns = [
    path('<username>/<slug:slug>', views.blurb_detail, name='blurb_detail'),
    path('<username>/create/', views.CreateBlurbView.as_view(), name='create_blurb'),
    path('feed/', views.blurbs_feed, name='blurbs_feed'),
]
