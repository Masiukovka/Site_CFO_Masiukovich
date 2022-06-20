from django.db import models


class blog(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)