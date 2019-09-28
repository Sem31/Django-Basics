from django.db import models

# Create your models here.
class Topic(models.Model) :
    top_name = models.CharField(max_length=50)

    def __str__(self):
        return self.top_name

class Webpage(models.Model) :
    category  = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class AccessRecord(models.Model) :
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.date)