# Generated by Django 2.1.2 on 2019-07-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20190719_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='forma_pago',
            field=models.CharField(blank=True, choices=[['PAGARE', 'Pagare'], ['TRANSFERENCIA', 'Transferencia']], default='TRANSFERENCIA', max_length=9, null=True, verbose_name='Forma de Pago'),
        ),
    ]
