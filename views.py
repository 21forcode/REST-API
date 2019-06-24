from rest_framework import generics
from .models import poat
from .serializers import appSerializer
from django.shortcuts import render
from rest_framework import viewsets

class ListappView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = poat.objects.all()
    serializer_class = appSerializer
