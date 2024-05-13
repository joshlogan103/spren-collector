from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Spren
from .serializers import SprenSerializer

# Create your views here.

class Home(APIView):
  def get(self, request):
    content = { 'message': 'Welcome to the Spren Collector!'}
    return Response(content)
  
class SprenList(generics.ListCreateAPIView):
  queryset = Spren.objects.all()
  serializer_class = SprenSerializer

class SprenDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Spren.objects.all()
  serializer_class = SprenSerializer
  lookup_field = 'id'
