from django.db import models

# Create your models here
class Topic(models.Model):
    topic = models.CharField(max_length=50,unique = True)

    def __str__(self):
        return self.topic


class Webpages(models.Model):
    name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    website = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class AccessRecords(models.Model):
    name = models.ForeignKey(Webpages, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.date)
