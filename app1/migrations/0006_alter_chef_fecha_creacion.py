# Generated by Django 4.1.2 on 2022-11-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_chef_fecha_creacion_chef_imagen_receta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
