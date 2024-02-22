from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название товара')
    description = models.TextField(verbose_name='описание товара')
    preview = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена товара')
    created_at = models.DateTimeField(verbose_name='дата создания')
    updated_at = models.DateTimeField(verbose_name='дата обновления')


    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'подукт'
        verbose_name_plural = 'продукты'
        ordering = ('name', 'description',)
