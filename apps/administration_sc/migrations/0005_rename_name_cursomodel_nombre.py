# Generated by Django 4.2 on 2023-04-22 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration_sc', '0004_estudiantemodel_contrasena'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursomodel',
            old_name='name',
            new_name='nombre',
        ),
    ]
