
from apps.administration_sc.models import profesorModel,estudianteModel
from apps.administration_sc.serializers.serializers import student_serializers,teacher_serializers

from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

# Create your views here.

# UPDATE ACTIONS ACCOUNT
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