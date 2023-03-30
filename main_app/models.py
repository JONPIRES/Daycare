from django.db import models
from django.urls import reverse
# Whenever a new model is created, you should also add it to the admin.py
# after creating or editing a model, you need to run the commands 'python3 manage.py makemigrations' and then
# 'python3 manage.py migrate' to implement the changes
MEALS = (
    ('B','Breakfast'),('L','Lunch'), ('D', 'Dinner')
)
# Create your models here.
SIZES = (
    ('S','Small'),('M','Medium'), ('L', 'Large')
)
class Toy(models.Model):
    name:models.CharField(max_length=50)
    size = models.CharField(
        max_length=1,
        choices = SIZES,
        default=SIZES[0][0]
        )
    color:models.CharField(max_length=10)

    def __str__(self):
        return self.name
    


class Kids(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        # you need to import reverse from jango /\/\
        # also to pass context to the page, you need to use kwargs(needs to be lowercase)
        return reverse('detail', kwargs ={'kid_id': self.id})

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices = MEALS,
        default=MEALS[0][0]
        )
    kid = models.ForeignKey(Kids, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    # over here I can set the order in whick I display the feedings, based on the date or which ever key I want.
    class META:
        ordering = ['-date']