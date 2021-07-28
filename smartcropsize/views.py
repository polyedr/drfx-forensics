from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from smartcropsize.models import SmartcropImage
from smartcropsize.serializers import SmartcropImageSerializer


class SmartcropImageList(generics.ListCreateAPIView):
    """
    List all project screens, or create a new project screen.
    """

    queryset = SmartcropImage.objects.all()
    serializer_class = SmartcropImageSerializer


class SmartcropImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a project screen
    """

    queryset = SmartcropImage.objects.all()
    serializer_class = SmartcropImageSerializer