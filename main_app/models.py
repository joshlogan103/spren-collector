from django.db import models
from datetime import date

# Create your models here.

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Spren(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=40)
  description = models.CharField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def fed_for_today(self):
    return self.feeding_set.filter(date = date.today()).count() >= len(MEALS)
  
class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices = MEALS,
    default=MEALS[0][0]
    )
  spren = models.ForeignKey(Spren, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']
