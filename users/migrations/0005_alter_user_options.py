# Generated by Django 4.2 on 2024-04-08 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_user_is_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
