from django.urls import path
from .views import ListappView


urlpatterns = [
    path('poat/', ListappView.as_view(), name="poat-all")
]
