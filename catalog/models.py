from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="наименование")
    description = models.TextField(max_length=100, verbose_name="описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="название товара")
    description = models.TextField(verbose_name="описание товара")
    preview = models.ImageField(
        upload_to="products/", verbose_name="изображение", **NULLABLE
    )
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="продавец",
        help_text="укажите продавца",
    )

    price = models.IntegerField(verbose_name="цена товара")
    created_at = models.DateTimeField(auto_now=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата обновления")

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        verbose_name = "подукт"
        verbose_name_plural = "продукты"
        ordering = (
            "name",
            "description",
        )


class Version(models.Model):
    """Модель версий"""

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="versions", verbose_name="товар"
    )
    version_number = models.IntegerField(verbose_name="номер версии")
    version_name = models.CharField(max_length=150, verbose_name="название версии")
    active = models.BooleanField(default=True, verbose_name="признак текущей версии")

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = "версия"
        verbose_name_plural = "версии"
