# Generated by Django 2.0.7 on 2019-08-20 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0020_auto_20190820_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='historico',
            name='kilos_actuales',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
    ]
