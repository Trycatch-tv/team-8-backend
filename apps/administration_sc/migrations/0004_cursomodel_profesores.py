# Generated by Django 4.2 on 2023-04-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration_sc', '0003_remove_cursomodel_profesores'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursomodel',
            name='profesores',
            field=models.ManyToManyField(to='administration_sc.profesormodel'),
        ),
    ]
