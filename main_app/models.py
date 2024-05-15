from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Power(models.Model):
  name = models.CharField(max_length=50)
  effect = models.CharField(max_length=100)
  color = models.CharField(max_length=30)

  def __str__(self):
    return self.name
  
class Radiant(models.Model):
  name = models.CharField(max_length=100)
  origin = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Power(models.Model):
  name = models.CharField(max_length=50)
  effect = models.CharField(max_length=100)
  color = models.CharField(max_length=30)

  def __str__(self):
    return self.name
  
class Radiant(models.Model):
  name = models.CharField(max_length=100)
  origin = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Spren(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=40)
  description = models.CharField(max_length=250)
  age = models.IntegerField()
  powers = models.ManyToManyField(Power)
  radiants = models.ManyToManyField(Radiant, through = 'Interaction')
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def fed_for_today(self):
    return self.feeding_set.filter(date = date.today()).count() >= len(MEALS)
  
class Interaction(models.Model):
  spren = models.ForeignKey(Spren, on_delete=models.CASCADE)
  radiants = models.ForeignKey(Radiant, on_delete=models.CASCADE)
  description = models.CharField(max_length=100)
  date = models.DateField('Interaction date')

  def __str__(self):
    return self.description
  
  class META:
    ordering=['-date']
  
class Interaction(models.Model):
  spren = models.ForeignKey(Spren, on_delete=models.CASCADE)
  radiants = models.ForeignKey(Radiant, on_delete=models.CASCADE)
  description = models.CharField(max_length=100)
  date = models.DateField('Interaction date')

  def __str__(self):
    return self.description
  
  class META:
    ordering=['-date']
  
class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices = MEALS,
    default=MEALS[0][0]
    )
  spren = models.ForeignKey(Spren, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_meal_display()} on {self.date} for {self.spren}"
    return f"{self.get_meal_display()} on {self.date} for {self.spren}"
  
  class Meta:
    ordering = ['-date']