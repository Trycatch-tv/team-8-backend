# Generated by Django 4.2.2 on 2023-07-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration_sc', '0002_remove_estudiantemodel_ciudad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantemodel',
            name='type_document',
            field=models.CharField(blank=True, choices=[('TI', 'Tarjeta Identidad'), ('DC', 'Cedula')], max_length=3),
        ),
    ]