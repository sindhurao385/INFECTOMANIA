

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.

class Disease(models.Model):

    country = models.CharField(max_length=120)
    total_cases = models.CharField(max_length=120)
    total_deaths = models.CharField(max_length=120)
    total_recovered = models.CharField(max_length=120)
    active_cases = models.CharField(max_length=120)

class Forum(models.Model):

    #user = models.ForiegnKey(User)
    username = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
    )
    #username = models.CharField(max_length=120)
    comment = models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    
    