from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers.serializers import *
from .models import *

# Create your views here.

class student_list(generics.ListCreateAPIView):
    queryset = estudianteModel.objects.all()
    serializer_class = student_serializers

class teacher_list(generics.ListCreateAPIView):
    queryset = profesorModel.objects.all()
    serializer_class = teacher_serializers
    
class course_list(generics.ListCreateAPIView):
    queryset = cursoModel.objects.all()
    serializer_class = course_serializers