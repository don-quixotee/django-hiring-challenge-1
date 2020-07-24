from django.db import models

# Create your models here.
class Scrawler(models.Model):
    webUrl = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name