from django.db import models

class About_me(models.Model):
    title = models.CharField(max_length=50, verbose_name='Период')
    content = models.TextField(max_length=200, verbose_name='Событие')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'

