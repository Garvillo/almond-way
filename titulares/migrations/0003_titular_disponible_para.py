# Generated by Django 2.2.1 on 2020-10-03 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titulares', '0002_titular_letra'),
    ]

    operations = [
        migrations.AddField(
            model_name='titular',
            name='disponible_para',
            field=models.CharField(choices=[['COMPRAS', 'Compras'], ['VENTAS', 'Ventas']], default='COMPRAS', max_length=50, verbose_name='indica si este titular esta disponible para comras o ventas'),
        ),
    ]
