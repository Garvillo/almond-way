# Generated by Django 2.1.2 on 2019-08-14 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agentes', '0001_initial'),
        ('titulares', '0002_titular_letra'),
        ('clientes', '0002_auto_20190703_2040'),
        ('productos', '0013_auto_20190812_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=7)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pago', models.CharField(choices=[['PAGARE', 'Pagare'], ['TRANSFERENCIA', 'Transferencia']], default='TRANSFERENCIA', max_length=50, verbose_name='Forma de Pago')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('nfact', models.IntegerField()),
                ('lfact', models.CharField(max_length=2)),
                ('imp_aplicado', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('base', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('agente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agentes.Agente')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente')),
                ('impuestos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Impuestos')),
                ('titular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='titulares.Titular')),
            ],
        ),
        migrations.RemoveField(
            model_name='detallecompra',
            name='total_detalle',
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Venta'),
        ),
    ]
