from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializer import *
from .models import *

# Create your views here.



class people_list(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class= PersonSerializer

class studentlist():
    queryset = estudianteModel.objects.all()
    serializer_class = studentSerializer