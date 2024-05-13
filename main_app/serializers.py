from rest_framework import serializers
from .models import Spren

class SprenSerializer(serializers.ModelSerializer):
  class Meta:
    model = Spren
    fields = '__all__'