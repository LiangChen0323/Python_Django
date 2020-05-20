from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True)
