# Generated by Django 4.2 on 2023-04-22 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration_sc', '0005_rename_name_cursomodel_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesormodel',
            name='contrasena',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]