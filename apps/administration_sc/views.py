from django.shortcuts import render
from rest_framework.generics import DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView,ListCreateAPIView,CreateAPIView
from rest_framework.decorators import api_view
from .serializers.serializers import *
from .models import *
import hashlib 
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password, make_password


# Create your views here.

from .backend_auth.backend_student import EstudianteBackend
from .backend_auth.backend_teacher import TeacherBackend
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
    

#ADD ACTIONS

class add_student(CreateAPIView):
    queryset = estudianteModel.objects.all()
    serializer_class = student_serializers

    def perform_create(self, serializer):
        # Obtener la contraseña del serializer
        contrasena = serializer.validated_data.get('contrasena')
        
        contrasena_hasheada = make_password(contrasena)
        
        serializer.save(contrasena=contrasena_hasheada)

class add_teacher(CreateAPIView):
    queryset = profesorModel.objects.all()
    serializer_class = teacher_serializers
    
    def perform_create(self, serializer):
        # Obtener la contraseña del serializer
        contrasena = serializer.validated_data.get('contrasena')
        
        contrasena_hasheada = make_password(contrasena)
        
        serializer.save(contrasena=contrasena_hasheada)
    
class add_course(CreateAPIView):
    queryset = cursoModel.objects.all()
    serializer_class = course_serializers



#Hacer Validaciones De Login de student y teacher, admin


class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if username is None or password is None:
            return Response({'message': 'Por favor ingrese un nombre de usuario y una contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({'message': 'Inicio de sesión exitoso.'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Esta cuenta está desactivada.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'El nombre de usuario o la contraseña son incorrectos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
class StudentLoginView(APIView):
    def post(self, request):
        email = request.data.get('correo')
        password = request.data.get('contrasena')

        if email is None or password is None:
            return Response({'message': 'Por favor ingrese un correo y una contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

        # Busca el estudiante con el correo electrónico proporcionado
        try:
            student = estudianteModel.objects.get(correo=email)

        except estudianteModel.DoesNotExist:
            return Response({'message': 'El correo electrónico o  la contraseña son incorrectos.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Autentica al estudiante utilizando su correo electrónico y contraseña
        estudiante = EstudianteBackend.authenticate_student(self,request,correo=email,contrasena=password)
        
        print(estudiante)

        if estudiante is not None:
            return Response({'message': 'Inicio de sesión exitoso.', 'correo':student.correo}, status=status.HTTP_200_OK,)
    
        else:
            return Response({'message': 'El correo electrónico o la contraseña son incorrectos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        
class TeacherLoginView(APIView):
    def post(self, request):
        email = request.data.get('correo')
        password = request.data.get('contrasena')

        if email is None or password is None:
            return Response({'message': 'Por favor ingrese un correo y una contraseña.','correo':profesor.correo}, status=status.HTTP_400_BAD_REQUEST)

        # Busca el estudiante con el correo electrónico proporcionado
        try:
            student = profesorModel.objects.get(correo=email)
        except profesorModel.DoesNotExist:
            return Response({'message': 'El correo electrónico o la contraseña son incorrectos.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Autentica al estudiante utilizando su correo electrónico y contraseña
        profesor = TeacherBackend.authenticate_teacher(self,request,correo=email,contrasena=password)

        if profesor is not None:
                return Response({'message': 'Inicio de sesión exitoso.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'El correo electrónico o la contraseña son incorrectos.'}, status=status.HTTP_401_UNAUTHORIZED)