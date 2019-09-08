# Generated by Django 2.0.7 on 2019-09-07 23:05

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0021_auto_20190820_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagareCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('numero', models.CharField(blank=True, max_length=25, null=True)),
                ('fecha_emitido', models.DateField(blank=True, default=True)),
                ('fecha_cobrado', models.DateField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('cobrado', models.BooleanField(default=False)),
                ('observaciones', models.CharField(blank=True, max_length=250, null=True)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Compra')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='PagareVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('fecha_emitido', models.DateField(blank=True, default=True)),
                ('numero', models.CharField(blank=True, max_length=25, null=True)),
                ('fecha_cobrado', models.DateField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('cobrado', models.BooleanField(default=False)),
                ('observaciones', models.CharField(blank=True, max_length=250, null=True)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Venta')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]