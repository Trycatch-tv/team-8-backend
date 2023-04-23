from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from ..models import estudianteModel
class EstudianteBackend(BaseBackend):
    def authenticate_student(self, request, correo=None, contrasena=None):
        try:
            estudiante = estudianteModel.objects.get(correo=correo)
            if check_password(contrasena,estudiante.contrasena):
                return estudiante
        except estudianteModel.DoesNotExist:
            return None

    def get_student(self, user_id):
        try:
            return estudianteModel.objects.get(pk=user_id)
        except estudianteModel.DoesNotExist:
            return None