# Generated by Django 2.0.7 on 2019-08-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_auto_20190806_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='base',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='imp_aplicado',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
