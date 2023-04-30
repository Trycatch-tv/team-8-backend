from rest_framework import serializers
from django.contrib.auth.hashers import  make_password
from ..models import *

class student_serializers(serializers.ModelSerializer):
    class Meta:
        model = estudianteModel
        fields = '__all__'
    def update(self, instance, validated_data):
        # Si la contraseña está presente en los datos validados, convertirla en hash usando make_password
        password = validated_data.get('password')
        if password is not None:
            validated_data['password'] = make_password(password)

        return super().update(instance, validated_data)
class teacher_serializers(serializers.ModelSerializer):
    class Meta:
        model = profesorModel
        fields = '__all__'
        
    def update(self, instance, validated_data):
        # Si la contraseña está presente en los datos validados, convertirla en hash usando make_password
        password = validated_data.get('password')
        if password is not None:
            validated_data['password'] = make_password(password)

        return super().update(instance, validated_data)    
class course_serializers(serializers.ModelSerializer):
    class Meta:
        model = cursoModel
        fields = '__all__'
  
        

