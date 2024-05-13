from rest_framework import serializers
from .models import Spren, Feeding, Power

class SprenSerializer(serializers.HyperlinkedModelSerializer):
  fed_for_today = serializers.SerializerMethodField()

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

class PowerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Power
    fields = '__all__'
    extra_kwargs = {'url': {'view_name': 'power-detail', 'lookup_field': 'id'}}
