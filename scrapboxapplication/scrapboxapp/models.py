from django.db import models

# Create your models here.

class ScrapBox(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField()
    category=models.CharField()