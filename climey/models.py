from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Good(models.Model):
    name = models.TextField()
    about = models.TextField()
    price = models.TextField()
    image = models.ImageField(upload_to='climey/images/', blank=False)

    def __str__(self):
        return f'{self.name}'