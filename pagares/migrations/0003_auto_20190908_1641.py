# Generated by Django 2.0.7 on 2019-09-08 16:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pagares', '0002_auto_20190908_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagareventa',
            name='fecha_emitido',
            field=models.DateField(default=datetime.datetime(2019, 9, 8, 16, 41, 11, 49410, tzinfo=utc)),
        ),
    ]
