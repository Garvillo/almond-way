# Generated by Django 2.0.7 on 2019-09-08 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pagares', '0003_auto_20190908_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagareventa',
            name='fecha_emitido',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
