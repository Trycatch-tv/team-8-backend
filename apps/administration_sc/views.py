from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializer import *
from .models import *

# Create your views here.

class student_list():
    queryset = estudianteModel.objects.all()
    serializer_class = student_serializers

class teacher_list():
    queryset = profesorModel.objects.all()
    serializer_class = teacher_serializers
    
class course_list():
    queryset = cursoModel.objects.all()
    serializer_class = course_serializers