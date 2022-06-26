from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Событие')
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='Фото')
    content = models.TextField(max_length=5000, verbose_name='Действие')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Состоялось')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=100)
