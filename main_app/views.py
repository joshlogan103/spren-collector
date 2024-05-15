from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied
from .models import Spren, Feeding, Power, Radiant, Interaction
from .serializers import SprenSerializer, FeedingSerializer, PowerSerializer, RadiantSerializer, InteractionSerializer, UserSerializer

# Create your views here.

class Home(APIView):
  def get(self, request):
    content = { 'message': 'Welcome to the Spren Collector!'}
    return Response(content)
  
class SprenList(generics.ListCreateAPIView):
  serializer_class = SprenSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    user = self.request.user # Only return Spren belonging to the user
    return Spren.objects.filter(user=user)
  
  def perform_create(self, serializer):
    # Associate newly created Spren to the user that created them
    serializer.save(user=self.request.user)

class SprenDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SprenSerializer
  lookup_field = 'id'

  def get_queryset(self):
    user = self.request.user
    return Spren.objects.filter(user=user)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance, context = {'request': request})

    powers_not_associated = Power.objects.exclude(id__in = instance.powers.all())
    powers_serializer = PowerSerializer(powers_not_associated, many = True, context = {'request': request})

    return Response({
      'spren': serializer.data,
      'powers_not_associated': powers_serializer.data
    })
  
  def perform_update(self, serializer):
    spren = self.get_object()
    if spren.user != self.request.user:
      raise PermissionDenied({'message': 'You do not have permission to edit this Spren.'})
    serializer.save()

  def perform_destroy(self, instance):
    if instance.user != self.request.user:
      raise PermissionDenied({'message': 'You do not have permission to delete this Spren.'})
    instance.delete()

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

# User Registration
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    response = super().create(request, *args, **kwargs)
    user = User.objects.get(username=response.data['username'])
    refresh = RefreshToken.for_user(user)
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': response.data
    })

# User Login
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]

  def post(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
      refresh = RefreshToken.for_user(user)
      return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user': UserSerializer(user).data
      })
    return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = User.objects.get(username=request.user)  # Fetch user profile
    refresh = RefreshToken.for_user(request.user)  # Generate new refresh token
    return Response({
      'refresh': str(refresh),
      'access': str(refresh.access_token),
      'user': UserSerializer(user).data
    })
