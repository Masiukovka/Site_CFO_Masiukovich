from django.db import models

# Create your models here.
class Main_paig(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    photo = models.ImageField(upload_to='photos/', verbose_name='Изображение')
    content = models.TextField(max_length=200, verbose_name='Пояснительный текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стартовый блок'
        verbose_name_plural = 'Стартовые блоки'
