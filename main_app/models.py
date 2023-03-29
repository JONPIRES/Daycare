from django.db import models
from django.urls import reverse
# after creating or editing a model, you need to run the commands 'python3 manage.py makemigrations' and then
# 'python3 manage.py migrate' to implement the changes

# Create your models here.

class Kids(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        # you need to import reverse from jango /\/\
        # also to pass context to the page, you need to use Kwargs
        return reverse('detail', Kwargs ={'cat_id': self.id})
