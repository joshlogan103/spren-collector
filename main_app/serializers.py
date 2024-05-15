from rest_framework import serializers
from .models import Spren, Feeding, Power, Radiant, Interaction
from django.contrib.auth.models import User

class PowerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Power
    fields = '__all__'
    extra_kwargs = {'url': {'view_name': 'power-detail', 'lookup_field': 'id'}}

class RadiantSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Radiant
    fields = '__all__'
    extra_kwargs = {'url': {'view_name': 'radiant-detail', 'lookup_field': 'id'}}

class SprenSerializer(serializers.HyperlinkedModelSerializer):
  fed_for_today = serializers.SerializerMethodField()
  powers = PowerSerializer(many = True, read_only = True)
  radiants = RadiantSerializer(many=True, read_only=True)
  user = serializers.PrimaryKeyRelatedField(read_only=True) # Make the user field read-only

  class Meta:
    model = Spren
    fields = '__all__'
    extra_kwargs = {'url': {'view_name': 'spren-detail', 'lookup_field': 'id'}}

  def get_fed_for_today(self, obj):
    return obj.fed_for_today()

class FeedingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Feeding
    fields = '__all__'
    read_only_fields = ('spren',)

class InteractionSerializer(serializers.ModelSerializer):
  spren = serializers.HyperlinkedRelatedField(
    view_name='spren-detail',
    read_only=True,
    lookup_field='id'
  )

  radiants = serializers.HyperlinkedRelatedField(
    view_name='radiant-detail',
    read_only=True,
    lookup_field='id'
  )

class InteractionSerializer(serializers.ModelSerializer):
  spren = serializers.HyperlinkedRelatedField(
    view_name='spren-detail',
    read_only=True,
    lookup_field='id'
  )

  radiants = serializers.HyperlinkedRelatedField(
    view_name='radiant-detail',
    read_only=True,
    lookup_field='id'
  )

  class Meta:
    model = Interaction
    model = Interaction
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)  # Add a password field, make it write-only
  spren = SprenSerializer(many = True, read_only = True)

  class Meta:
      model = User
      fields = ('id', 'username', 'email', 'password')
  
  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data['username'],
      email=validated_data['email'],
      password=validated_data['password']  # Ensures the password is hashed correctly
    )
    
    return user
