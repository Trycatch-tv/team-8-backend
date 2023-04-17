from django.db import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class estudianteModel(serializers.Serializers):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField(max_length=60)
    


class profesorModel(serializers.Serializers):
    pass

class cursoModel(serializers.Serializers):
    #name= models.CharField(max_length=90)
    #created_at = models.DateTimeField(auto_now=True)
    #valoraciones = models.ForeignKey(estudianteModel)
    
    
    
    pass
