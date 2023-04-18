from django.shortcuts import render
from rest_framework.generics import DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView,ListCreateAPIView
from rest_framework.decorators import api_view
from .serializers.serializers import *
from .models import *

# Create your views here.


# ADD ACTIONS
class student_list(ListCreateAPIView):
    queryset = estudianteModel.objects.all()
    serializer_class = student_serializers

class teacher_list(ListCreateAPIView):
    queryset = profesorModel.objects.all()
    serializer_class = teacher_serializers
    
class course_list(ListCreateAPIView):
    queryset = cursoModel.objects.all()
    serializer_class = course_serializers




# UPDATE ACTIONS
class update_student(RetrieveUpdateAPIView):
    queryset = estudianteModel.objects.all()
    serializer_class = student_serializers
    
    
class update_course(RetrieveUpdateAPIView):
    queryset = cursoModel.objects.all()
    serializer_class = course_serializers
    
class update_teacher(RetrieveUpdateAPIView):
    queryset = profesorModel.objects.all()
    serializer_class = teacher_serializers
    
    
#DELETE ACTIONS
    
class delete_student(DestroyAPIView):
    queryset = estudianteModel.objects.all()
    serializer_class = student_serializers
    
    
class delete_teacher(UpdateAPIView):
    queryset = profesorModel.objects.all()
    serializer_class = teacher_serializers
    
class delete_course(UpdateAPIView):
    queryset = cursoModel.objects.all()
    serializer_class = course_serializers