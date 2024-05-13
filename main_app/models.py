from django.db import models

# Create your models here.

class Spren(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=40)
  description = models.CharField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
