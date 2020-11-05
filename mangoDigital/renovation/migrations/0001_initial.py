# Generated by Django 3.1.2 on 2020-10-30 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BussinessContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessName', models.CharField(blank=True, max_length=25, null=True, verbose_name='Nombre del negocio')),
                ('businessWeb', models.CharField(blank=True, max_length=25, null=True, verbose_name='Sitio web')),
                ('businessUnit', models.CharField(blank=True, choices=[(None, '--------'), ('1 - 20', '1 - 20'), ('20 - 50', '20 - 50'), ('50 - 100', '50 - 100'), ('100 - 200', '100 - 200')], max_length=15, null=True, verbose_name='Empleados')),
                ('businessDir', models.CharField(blank=True, max_length=25, null=True, verbose_name='Dirección')),
                ('businessPhone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Teléfono')),
                ('description', models.TextField(blank=True, max_length=100, null=True, verbose_name='Descripción')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
            ],
        ),
    ]
