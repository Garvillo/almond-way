# Generated by Django 2.2.1 on 2020-07-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0004_auto_20190908_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='ciudad',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='codigo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='contacto',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='diaspago',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='domicilia',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='fax',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='formapago',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='movil',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='observaciones',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='url',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
