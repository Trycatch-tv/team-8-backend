from rest_framework import serializers

from ..models import *

class student_serializers(serializers.ModelSerializer):
    class Meta:
        model = estudianteModel
        fields = '__all__'
        
class teacher_serializers(serializers.ModelSerializer):
    class Meta:
        model = profesorModel
        fields = '__all__'
class course_serializers(serializers.ModelSerializer):
    class Meta:
        model = cursoModel
        fields = '__all__'
        

