# Generated by Django 2.0.7 on 2019-05-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cif', models.CharField(max_length=11, unique=True)),
                ('razon_social', models.CharField(max_length=150)),
                ('direccion', models.CharField(blank=True, max_length=200, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('moroso', models.BooleanField(default=False)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
