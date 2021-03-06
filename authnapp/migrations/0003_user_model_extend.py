# Generated by Django 3.2.12 on 2022-04-14 16:36

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("authnapp", "0002_alter_shopuser_age"),
    ]

    operations = [
        migrations.AddField(
            model_name="shopuser",
            name="activation_key",
            field=models.CharField(blank=True, max_length=128, verbose_name="ключ подтверждения"),
        ),
        migrations.AddField(
            model_name="shopuser",
            name="activation_key_expires",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 4, 16, 16, 36, 2, 738906, tzinfo=utc), verbose_name="актуальность ключа"
            ),
        ),
        migrations.AlterField(
            model_name="shopuser",
            name="age",
            field=models.PositiveIntegerField(verbose_name="возраст"),
        ),
    ]
