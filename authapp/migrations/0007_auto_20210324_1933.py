# Generated by Django 2.2.17 on 2021-03-24 19:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210322_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 26, 19, 33, 31, 694323, tzinfo=utc)),
        ),
    ]
