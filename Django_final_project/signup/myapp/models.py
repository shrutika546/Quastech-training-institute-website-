from django.db import models

# Create your models here.
class user_model(models.Model):
    objects = None
    username=models.CharField(max_length=20)
    email = models.EmailField()
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

