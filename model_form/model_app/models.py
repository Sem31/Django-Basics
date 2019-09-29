from django.db import models

# Create your models here.


class User1(models.Model):
    first_name = models.CharField(max_length=50,unique = True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
