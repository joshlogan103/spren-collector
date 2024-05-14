from rest_framework import serializers
from .models import Spren, Feeding, Power, Radiant, Interaction

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

  class Meta:
    model = Interaction
    fields = '__all__'
