# Generated by Django 2.0.7 on 2019-08-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titular',
            name='letra',
            field=models.CharField(default='A', max_length=2),
        ),
    ]
