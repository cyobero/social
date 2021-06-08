from django.urls import path
from .views import BlurbDetailView

urlpatterns = [
    path('<username>/<slug:slug>', BlurbDetailView.as_view(), name='blurb_detail')
]
