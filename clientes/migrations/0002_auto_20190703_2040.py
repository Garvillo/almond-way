# Generated by Django 2.0.7 on 2019-07-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='moroso',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cif',
            field=models.CharField(max_length=15),
        ),
    ]
