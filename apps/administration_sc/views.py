from django.shortcuts import render
from rest_framework.generics import DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView,ListCreateAPIView,CreateAPIView,ListAPIView
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
from django.http import JsonResponse

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
    
    def get(self, request, *args, **kwargs):
        print("pass")
        # Obtiene el ID del estudiante de los parámetros de la solicitud
        id_estudiante = kwargs.get('pk')
        # Consulta el objeto estudiante con el ID especificado
        estudiante = self.queryset.filter(id=id_estudiante).first()
        # Verifica si el objeto existe
        if not estudiante:
            return Response({"error": "El estudiante no existe"}, status=status.HTTP_404_NOT_FOUND)
        # Serializa el objeto estudiante y devuelve los datos
        serializer = self.serializer_class(estudiante)
        return Response(serializer.data)
    
class update_course(RetrieveUpdateAPIView):
    queryset = cursoModel.objects.all()
    serializer_class = course_serializers
    
    def get(self, request, *args, **kwargs):
        print("pass")
        # Obtiene el ID del estudiante de los parámetros de la solicitud
        id_course = kwargs.get('pk')
        # Consulta el objeto estudiante con el ID especificado
        course = self.queryset.filter(id=id_course).first()
        # Verifica si el objeto existe
        if not course:
            return Response({"error": "El course no existe"}, status=status.HTTP_404_NOT_FOUND)
        # Serializa el objeto estudiante y devuelve los datos
        serializer = self.serializer_class(course)
        return Response(serializer.data)
class update_teacher(RetrieveUpdateAPIView):
    queryset = profesorModel.objects.all()
    serializer_class = teacher_serializers
    
    def get(self, request, *args, **kwargs):
        print("pass")
        # Obtiene el ID del estudiante de los parámetros de la solicitud
        id_teacher = kwargs.get('pk')
        # Consulta el objeto estudiante con el ID especificado
        teacher = self.queryset.filter(id=id_teacher).first()
        # Verifica si el objeto existe
        if not teacher:
            return Response({"error": "El teacher no existe"}, status=status.HTTP_404_NOT_FOUND)
        # Serializa el objeto estudiante y devuelve los datos
        serializer = self.serializer_class(teacher)
        return Response(serializer.data)
    
    
#DELETE ACTIONS
    
class delete_student(DestroyAPIView):
    queryset = estudianteModel.objects.all()
    serializer_class = student_serializers
    
    
class delete_teacher(DestroyAPIView):
    queryset = profesorModel.objects.all()
    serializer_class = teacher_serializers
    
class delete_course(DestroyAPIView):
    queryset = cursoModel.objects.all()
    serializer_class = course_serializers
    

#ADD ACTIONS

class add_student(CreateAPIView):
    queryset = estudianteModel.objects.all()
    serializer_class = student_serializers
    
    

    def perform_create(self, serializer):
        
        print("Heyyy Hp")
        # Obtener la contraseña del serializer
        contrasena = serializer.validated_data.get('contrasena')
        
        print(contrasena)
        
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
                return Response({'message': 'Inicio de sesión exitoso.','username':user.username}, status=status.HTTP_200_OK)
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
            return Response({'message': 'Inicio de sesión exitoso.', 'correo':student.correo,'nombre':student.nombre, 'id':student.id,'rol':student.rol}, status=status.HTTP_200_OK,)
    
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
                return Response({'message': 'Inicio de sesión exitoso.','correo':profesor.correo,'id':profesor.id,'rol':profesor.rol,'nombre':profesor.nombre}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'El correo electrónico o la contraseña son incorrectos.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        


# Helpers 



class TeacherStudent(ListAPIView):
    serializer_class = student_serializers

    def get_queryset(self):
        id_profesor = self.kwargs['id']
        return estudianteModel.objects.filter(id_profesor=id_profesor)
    

class TeacherCourse(ListAPIView):
    serializer_class = teacher_serializers

    def get_queryset(self):
        id_curso = self.kwargs['id']
        profesorModel.objects.filter(id_curso = id_curso)
        return profesorModel.objects.filter(id_curso=id_curso)
    
    

class StudentCourse(ListAPIView):
    serializer_class = course_serializers

    def get_queryset(self):
        id_student = self.kwargs['id']
        cursoModel.objects.filter(id_student = id_student)
        return cursoModel.objects.filter(id_student=id_student)
    
    
@api_view(['POST'])
def agregar_curso_profesor_a_estudiante(request):
    # Obtener los datos del request
    id_curso = request.data.get('cursos')
    id_profesor = request.data.get('profesores')
    id_estudiante = request.data.get('studiantes')
    
    
    print(id_estudiante)
    
    curso = cursoModel.objects.get(id=id_curso)
    curso.estudiantes.add(id_estudiante)

    
    estudiante = estudianteModel.objects.get(id=id_estudiante)


    ##Agregar aca el teacher
    teacher = profesorModel.objects.get(id=id_profesor[0])
    teacher.estudiantes.add(id_estudiante)
    
    # Agregar los objetos al estudiante
    estudiante.cursos.add(id_curso)
    estudiante.profesores.add(id_profesor[0])


    # Retornar una respuesta exitosa
    return Response({'mensaje': 'Curso y profesor agregados al estudiante exitosamente.'})


@api_view(['POST'])
def agregar_curso_profesor(request):
    #Obtener los datos del request
    id_teacher = request.data.get('profesores')
    id_curso = request.data.get('cursos')
    
    
    curso = cursoModel.objects.get(id=id_curso)
    curso.profesores.add(id_teacher)
    
    teacher = profesorModel.objects.get(id=id_teacher)
    teacher.cursos.add(id_curso)
    
    
    return Response({'mensaje': 'Curso y profesor agregados al estudiante exitosamente.'})

    



class CursosEstudianteView(APIView):
    def get(self, request, estudiante_id):
        cursos = cursoModel.objects.filter(estudiantes=estudiante_id).values()
        
        return JsonResponse({'cursos': list(cursos)})



class ProfesorCursosView(APIView):
    def get(self,request,profesor_id):
        cursos = cursoModel.objects.filter(profesores=profesor_id).values()
        
        return JsonResponse({'courses_teacher':list(cursos)})
    
    
class ProfesorEstudiantes(APIView):
    def get(self,request,profesor_id):
        estudiantes = estudianteModel.objects.filter(profesores=profesor_id).values()
        
        return JsonResponse({'students':list(estudiantes)})
##Add View of one students return json data

