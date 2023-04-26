from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _


class categoria_choices(models.TextChoices):
    OPCION_1 = 'Academico', _('Academico')
    OPCION_2 = 'Tecnologico', _('Tecnologico')

class nivel_choices(models.TextChoices):
    OPCION_1 = 'Basico', _('Basico')
    OPCION_2 = 'Intermedio', _('Intermedio')
    OPCION_3 = 'Avanzado' ,('Avanzado')


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

class cursoModel(models.Model):
    nombre = models.CharField(max_length=90)
    categoria = models.CharField(
        choices=categoria_choices.choices,
        default=categoria_choices.OPCION_1,
        max_length=11,
        blank=True
    )
    nivel_curso = models.CharField(
        choices=nivel_choices.choices,
        default=nivel_choices.OPCION_1,
        max_length=11,
                blank=True

    )
    numero_max_estudiantes = models.IntegerField(blank=True, null=True)
    codigo_curso = models.CharField(max_length=30,blank=True)
    created_at = models.DateField(auto_now=True)
    valoraciones = models.ForeignKey('estudianteModel', on_delete=models.CASCADE, related_name='curso_estudent_vc')
    id_estudiante = models.ForeignKey('estudianteModel', on_delete=models.CASCADE , related_name='curso_estudent', null=True,blank=True)
    id_profesor = models.ForeignKey('profesorModel', on_delete=models.CASCADE, related_name='curso_teacher', null=True,blank=True)     
    estado = models.CharField(max_length=15)
    
    
    def __str__(self) -> str:
        return self.nombre

class profesorModel(models.Model):
    nombre = models.CharField(max_length=90)
    correo = models.EmailField(max_length=60)
    telefono = models.IntegerField()
    descripcion = models.TextField()
    area_especializacion = models.CharField(max_length=50)
    id_estudiante = models.ForeignKey('estudianteModel', on_delete=models.CASCADE, related_name='estudent_teacher',null=True,blank=True)
    id_curso = models.ForeignKey(cursoModel, on_delete=models.CASCADE, related_name='curso_teacher',null=True,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=90, blank=True,null=True)
    rol = models.CharField(max_length=20, blank=True,null=True)

    
    
    
    def __str__(self) -> str:
        return self.nombre

class estudianteModel(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField(max_length=60)
    ciudad = models.CharField(choices=ciudad_choices.choices,
                              default=ciudad_choices.OPCION_1,
                              max_length=14,
                              )
    telefono = models.IntegerField()
    estado = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    id_curso = models.ForeignKey(cursoModel, on_delete=models.CASCADE , related_name='estudent_curso',null=True,blank=True)
    id_profesor = models.ForeignKey(profesorModel, on_delete=models.CASCADE, related_name='estudiante_teacher',null=True,blank=True)
    contrasena= models.CharField(max_length=90, blank=True, null=True)
    rol = models.CharField(max_length=20, blank=True,null=True)
    
    def __str__(self) -> str:
        return self.nombre
    
    



  
