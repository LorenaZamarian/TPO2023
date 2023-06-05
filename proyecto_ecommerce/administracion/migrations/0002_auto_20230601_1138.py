# Generated by Django 3.2.18 on 2023-06-01 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='ubicacion',
            field=models.CharField(max_length=50, verbose_name='Ubicacion'),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('precio', models.FloatField(max_length=6, verbose_name='Precio')),
                ('stock', models.CharField(max_length=10, null=True, verbose_name='Stock')),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('cosecha', models.CharField(max_length=10, null=True, verbose_name='Cosecha')),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administracion.bodega')),
                ('varietal', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administracion.varietal')),
            ],
        ),
    ]
