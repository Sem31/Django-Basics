from django.db import models

# Create your models here.

class User(models.Model) :
    Name = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)

    def __str__(self):
        return self.Name

class AccessRecord(models.Model) :
    Name = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.date)
