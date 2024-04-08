# Generated by Django 4.2 on 2024-04-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_alter_blogpost_creation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="creation_date",
            field=models.DateField(
                blank=True,
                default="2024-04-08",
                null=True,
                verbose_name="дата создания",
            ),
        ),
    ]
