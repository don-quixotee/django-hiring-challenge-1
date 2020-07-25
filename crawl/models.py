from django.db import models

# Create your models here.
class Scrawler(models.Model):
    webUrl = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    def __str__(self):
        return self.name