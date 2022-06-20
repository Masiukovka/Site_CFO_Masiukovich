from django.db import models

# Create your models here.
class Main_paig(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/')
    content = models.TextField(max_length=200)