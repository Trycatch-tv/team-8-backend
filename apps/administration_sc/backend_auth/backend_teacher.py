from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from ..models import profesorModel
class TeacherBackend(BaseBackend):
    def authenticate_teacher(self, request, correo=None, contrasena=None):
        try:
            profesor = profesorModel.objects.get(correo=correo)
            if check_password(contrasena, profesor.contrasena):
                return profesor
        except profesorModel.DoesNotExist:
            return None

    def get_teacher(self, user_id):
        try:
            return profesorModel.objects.get(pk=user_id)
        except profesorModel.DoesNotExist:
            return None