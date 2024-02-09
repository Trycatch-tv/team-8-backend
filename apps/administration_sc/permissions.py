from rest_framework.permissions import BasePermission
from .models import estudianteModel  # Asegúrate de importar tu modelo de estudiantes

class IsAuthenticatedEstudiante(BasePermission):
    def has_permission(self, request, view):
        print(request)
        # Verificar si el estudiante está autenticado y si es un estudiante
        estudiante = request.estudiante  # Suponiendo que has asignado el estudiante autenticado al atributo 'estudiante' del objeto request

        if not estudiante:
            return False

        # Asegúrate de ajustar este campo 'es_estudiante' según tu modelo estudiantesmodel
        return estudiante.es_estudiante