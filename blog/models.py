from django.db import models
import datetime

NULLABLE = {"null": True, "blank": True}


class BlogPost(models.Model):
    """Модель блоговой записи"""

    title = models.CharField(max_length=150, verbose_name="заголовок")
    content = models.TextField(verbose_name="содержимое")
    preview = models.ImageField(**NULLABLE, verbose_name="изображение")
    creation_date = models.DateField(
        default=datetime.date.today().isoformat(),
        **NULLABLE,
        verbose_name="дата создания"
    )
    #  Признак публикации
    publication_sign = models.BooleanField(default=False, verbose_name="опубликовано")
    views = models.IntegerField(default=0, verbose_name="колличество просмотров")
    slug = models.CharField(max_length=150, verbose_name="slug", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
