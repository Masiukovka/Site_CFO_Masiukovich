from django.db import models

class Uslugi(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(max_length=1000, verbose_name='Уточнение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'