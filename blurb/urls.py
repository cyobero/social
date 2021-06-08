from django.urls import path
from .views import BlurbDetailView, CreateBlurbView

urlpatterns = [
    path('<username>/<slug:slug>', BlurbDetailView.as_view(), name='blurb_detail'),
    path('<username>/create/', CreateBlurbView.as_view(), name='create_blurb'),
]
