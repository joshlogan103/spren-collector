from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Spren, Feeding, Power, Radiant, Interaction
from .serializers import SprenSerializer, FeedingSerializer, PowerSerializer, RadiantSerializer, InteractionSerializer

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

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance, context = {'request': request})

    powers_not_associated = Power.objects.exclude(id__in = instance.powers.all())
    powers_serializer = PowerSerializer(powers_not_associated, many = True, context = {'request': request})

    return Response({
      'spren': serializer.data,
      'powers_not_associated': powers_serializer.data
    })

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
  
class PowerList(generics.ListCreateAPIView):
  queryset = Power.objects.all()
  serializer_class = PowerSerializer

class PowerDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Power.objects.all()
  serializer_class = PowerSerializer
  lookup_field = 'id'

class AddPowerToSpren(APIView):
  def post(self, request, spren_id, power_id):
    spren = Spren.objects.get(id=spren_id)
    power = Power.objects.get(id=power_id)
    spren.powers.add(power)
    return Response ({
      'message': f"Power of {power.name} added to {spren.name}"
    })
  
class RemovePowerFromSpren(APIView):
  def delete(self, request, spren_id, power_id):
    spren = Spren.objects.get(id = spren_id)
    power = Power.objects.get(id = power_id)
    spren.powers.remove(power)
    return Response ({
      'message': f"Power of {power.name} removed from {spren.name} "
    })

class RadiantList(generics.ListCreateAPIView):
  queryset = Radiant.objects.all()
  serializer_class = RadiantSerializer

class RadiantDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Radiant.objects.all()
  serializer_class = RadiantSerializer
  lookup_field = 'id'

class InteractionList(generics.ListCreateAPIView):
  queryset = Interaction.objects.all()
  serializer_class = InteractionSerializer

  def get_queryset(self):
    spren_id = self.kwargs['spren_id']
    radiant_id = self.kwargs['radiant_id']
    return Interaction.objects.filter(spren_id = spren_id, radiants_id = radiant_id)
  
  def perform_create(self, serializer):
    spren_id = self.kwargs['spren_id']
    radiant_id = self.kwargs['radiant_id']
    spren = Spren.objects.get(id = spren_id)
    radiants = Radiant.objects.get(id = radiant_id)
    serializer.save(spren = spren, radiants = radiants)

class InteractionDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Interaction.objects.all()
  serializer_class = InteractionSerializer
  lookup_field = 'id'
