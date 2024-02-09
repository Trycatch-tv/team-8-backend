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


class type_document_choices(models.TextChoices):
    OPCION_1 = 'TI',_('Tarjeta Identidad'),
    OPCION_2 = 'DC',_('Cedula')
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
    estudiantes= models.ManyToManyField('estudianteModel',blank=True,null=True)
    profesores = models.ManyToManyField('profesorModel',blank=True,null=True)
    estado = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    
    
    def __str__(self) -> str:
        return str(self.id)

class profesorModel(models.Model):
    nombre = models.CharField(max_length=90)
    correo = models.EmailField(max_length=60)
    telefono = models.IntegerField()
    descripcion = models.TextField()
    area_especializacion = models.CharField(max_length=50)
    estudiantes= models.ManyToManyField('estudianteModel',blank=True,null=True)
    cursos = models.ManyToManyField(cursoModel,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=90, blank=True,null=True)
    rol = models.CharField(max_length=20, blank=True,null=True)

    
    
    
    def __str__(self) -> str:
        return str(self.id)

class estudianteModel(models.Model):
    
    type_document = models.CharField(max_length=3,blank=True,
        choices=type_document_choices.choices,
    )
    number_document = models.CharField(max_length=11,blank=True)
    identificacion_name = models.CharField(max_length=200,blank=True)
    full_name = models.CharField(max_length=100,blank=True)
    email_unique = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=20,blank=True)
    departments = models.CharField(max_length=50,blank=True)
    password = models.CharField(max_length=1000,blank=True)
    #avatar = models.ImageField('avatar')
    
    """
    nombre = models.CharField(max_length=60)
    correo = models.EmailField(max_length=60)
    ciudad = models.CharField(choices=ciudad_choices.choices,
                              default=ciudad_choices.OPCION_1,
                              max_length=14,
                              )
    telefono = models.IntegerField()
    estado = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    cursos = models.ManyToManyField(cursoModel,blank=True,null=True)
    profesores = models.ManyToManyField(profesorModel, blank=True,null=True)
    contrasena= models.CharField(max_length=200, blank=True, null=True)
    rol = models.CharField(max_length=20, blank=True,null=True)
    """
    def __str__(self) -> str:
        return str(self.id)
    
    



  
