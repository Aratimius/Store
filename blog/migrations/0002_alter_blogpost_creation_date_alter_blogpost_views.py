# Generated by Django 5.0.2 on 2024-03-14 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='creation_date',
            field=models.DateField(blank=True, default='2024-03-14', null=True, verbose_name='дата создания'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='колличество просмотров'),
        ),
    ]
