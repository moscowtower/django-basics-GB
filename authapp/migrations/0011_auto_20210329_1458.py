# Generated by Django 2.2.17 on 2021-03-29 14:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20210329_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 14, 57, 45, 46270, tzinfo=utc)),
        ),
    ]
