# Generated by Django 2.0.7 on 2019-09-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagarecompra',
            name='fecha_emitido',
            field=models.DateField(blank=True, null=True),
        ),
    ]