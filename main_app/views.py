from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Spren, Feeding
from .serializers import SprenSerializer, FeedingSerializer

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

class FeedingListCreate(generics.ListCreateAPIView):
  serializer_class = FeedingSerializer

  def get_queryset(self):
    spren_id = self.kwargs['spren_id']
    return Feeding.objects.filter(spren_id = spren_id)
  
  def perform_create(self, serializer):
    spren_id = self.kwargs['spren_id']
    spren = Spren.objects.get(id = spren_id)
    serializer.save(spren = spren)

class FeedingDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = FeedingSerializer
  lookup_field = 'id'

  def get_queryset(self):
    spren_id = self.kwargs['spren_id']
    return Feeding.objects.filter(spren_id = spren_id)
