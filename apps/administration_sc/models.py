from django.db import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.utils.translation import gettext as _

class ciudad_choices(models.TextChoices):
    OPCION_1 = 'Colombia', _('Colombia')
    OPCION_2 = 'Estados Unidos', _('EEUU')
    OPCION_3 = 'Espana', _('España')
    OPCION_4 = 'Mexico', _('Mexico')
    OPCION_5 = 'Peru', _('Peru')
    OPCION_6 = 'Canada', _('Canada')
    OPCION_7 = 'Inglaterra', _('Inglaterra')
    OPCION_8 = 'Italia', _('Italia')
    OPCION_9 = 'Venezuela', _('Venezuela')
    OPCION_10 = 'Chile', _('Chile')
    OPCION_11 = 'Panama', _('Panama')

class estudianteModel(serializers.Serializers):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField(max_length=60)
    ciudad = models.TextChoices(choice=ciudad_choices)
    telefono = models.IntegerField()
    estado = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    id_curso = models.ForeignKey(cursoModel, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre

class profesorModel(serializers.Serializers):
    nombre = models.CharField(max_length=90)
    correo = models.EmailField(max_length=60)
    telefono = models.IntegerField()
    descripcion = models.TextField()
    area_especializacion = models.CharField(max_length=50)
    id_estudiante = models.ForeignKey(estudianteModel)
    id_curso = models.ForeignKey(cursoModel)
    created_at = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=15)
    

class cursoModel(serializers.Serializers):
    name = models.CharField(max_length=90)
    creted_at = models.DateField(auto_now=True)
    valoraciones = models.ForeignKey(estudianteModel)
    id_estudiante = models.ForeignKey(estudianteModel)
    id_profesor = models.ForeignKey(profesorModel)     
    estado = models.CharField(max_length=15)
    

