from django.urls import path
from .views import blurb_detail, CreateBlurbView

urlpatterns = [
    path('<username>/<slug:slug>', blurb_detail, name='blurb_detail'),
    path('<username>/create/', CreateBlurbView.as_view(), name='create_blurb'),
]
