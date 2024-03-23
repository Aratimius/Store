# Generated by Django 5.0.2 on 2024-03-23 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_rename_is_active_version_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product', verbose_name='товар'),
        ),
    ]
