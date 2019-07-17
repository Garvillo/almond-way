# Generated by Django 2.0.7 on 2019-05-29 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificadoEco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor_certificado', models.CharField(max_length=150)),
                ('nombre', models.CharField(max_length=150)),
                ('fecha_inicio', models.DateField(auto_now_add=True, null=True)),
                ('fecha_fin', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=11, unique=True)),
                ('razon_social', models.CharField(max_length=150)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('certificado_eco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.CertificadoEco')),
            ],
        ),
    ]
