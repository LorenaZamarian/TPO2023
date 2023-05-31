# Generated by Django 3.2.18 on 2023-05-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('ubicacion', models.CharField(max_length=20, verbose_name='Ubicacion')),
                ('telefono', models.CharField(max_length=20, verbose_name='Telefono')),
                ('email', models.EmailField(max_length=150, null=True)),
                ('baja', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Varietal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('baja', models.BooleanField(default=0)),
            ],
        ),
    ]