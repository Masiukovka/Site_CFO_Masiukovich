from django.db import models

class uslugi(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
